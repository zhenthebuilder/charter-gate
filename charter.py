#!/usr/bin/env python3
"""charter — deliverable contracts for AI agents.

Declare the deliverables of a long-horizon agent task as a machine-checkable
contract (charter.toml). Gate any agent command through verify -> repair loops.
Keep a tamper-evident audit log of every attempt.

Stdlib only. Python >= 3.11 (tomllib).

Usage:
  charter init                      # scaffold charter.toml
  charter verify [-c charter.toml]  # check the contract, exit 1 on breach
  charter run [-c ...] [--max-repairs N] -- <agent command...>
  charter log                       # print the audit trail
"""

from __future__ import annotations

import argparse
import datetime as _dt
import fnmatch
import glob as _glob
import hashlib
import json
import os
import re
import shlex
import subprocess
import sys
import tomllib

__version__ = "0.1.0"

CHARTER_DIR = ".charter"
AUDIT_FILE = "audit.jsonl"
VIOLATIONS_FILE = "violations.md"

TEMPLATE = """\
# charter.toml — deliverable contract for an agent task.
# Run `charter verify` to check it; `charter run -- <agent cmd>` to gate an agent.

[charter]
name = "my-task"

# One [[deliverable]] block per artifact the agent must produce.
[[deliverable]]
id = "report"
path = "out/report.md"          # exact path or glob
min_bytes = 200                  # optional: reject stubs
must_match = ["## Results"]     # optional: regexes that MUST appear
must_not_match = ["TODO", "FIXME", "lorem ipsum"]  # regexes that must NOT appear

# Optional executable acceptance checks (exit 0 = pass).
[[check]]
id = "tests"
cmd = "python -m pytest -q"
timeout = 600
"""


def _now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def load_charter(path: str) -> dict:
    with open(path, "rb") as f:
        data = tomllib.load(f)
    if "deliverable" not in data and "check" not in data:
        raise SystemExit(f"charter: {path} declares no [[deliverable]] or [[check]] blocks")
    return data


# ---------------------------------------------------------------- verification

def _check_deliverable(d: dict, root: str) -> list[dict]:
    """Return a list of violation dicts for one deliverable."""
    vid = d.get("id", d.get("path", "?"))
    out: list[dict] = []

    def viol(kind: str, detail: str) -> None:
        out.append({"deliverable": vid, "kind": kind, "detail": detail})

    pattern = d.get("path")
    if not pattern:
        viol("config", "deliverable has no `path`")
        return out
    matches = sorted(_glob.glob(os.path.join(root, pattern), recursive=True))
    matches = [m for m in matches if os.path.isfile(m)]
    if not matches:
        viol("missing", f"no file matches `{pattern}`")
        return out
    min_count = int(d.get("min_count", 1))
    if len(matches) < min_count:
        viol("count", f"`{pattern}` matched {len(matches)} file(s); need >= {min_count}")

    min_bytes = int(d.get("min_bytes", 0))
    for m in matches:
        size = os.path.getsize(m)
        if size < min_bytes:
            viol("too_small", f"{os.path.relpath(m, root)} is {size} bytes; need >= {min_bytes}")

    must = d.get("must_match", [])
    forbid = d.get("must_not_match", [])
    if must or forbid:
        for m in matches:
            try:
                text = open(m, "r", encoding="utf-8", errors="replace").read()
            except OSError as e:
                viol("unreadable", f"{m}: {e}")
                continue
            rel = os.path.relpath(m, root)
            for rx in must:
                if not re.search(rx, text, re.MULTILINE):
                    viol("must_match", f"{rel}: required pattern not found: {rx!r}")
            for rx in forbid:
                hit = re.search(rx, text, re.MULTILINE)
                if hit:
                    viol("must_not_match", f"{rel}: forbidden pattern found: {rx!r} (e.g. {hit.group(0)[:60]!r})")

    max_age = d.get("max_age_minutes")
    if max_age is not None:
        import time
        for m in matches:
            age_min = (time.time() - os.path.getmtime(m)) / 60.0
            if age_min > float(max_age):
                viol("stale", f"{os.path.relpath(m, root)} is {age_min:.0f} min old; max {max_age}")
    return out


def _run_check(c: dict, root: str) -> tuple[list[dict], dict]:
    cid = c.get("id", c.get("cmd", "?"))
    cmd = c.get("cmd")
    timeout = float(c.get("timeout", 600))
    meta = {"check": cid, "cmd": cmd}
    if not cmd:
        return [{"deliverable": cid, "kind": "config", "detail": "check has no `cmd`"}], meta
    try:
        p = subprocess.run(cmd, shell=True, cwd=root, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        meta["result"] = "timeout"
        return [{"deliverable": cid, "kind": "check_timeout", "detail": f"`{cmd}` exceeded {timeout:.0f}s"}], meta
    meta["result"] = f"exit {p.returncode}"
    if p.returncode != 0:
        tail = (p.stdout + "\n" + p.stderr).strip()[-2000:]
        return [{"deliverable": cid, "kind": "check_failed",
                 "detail": f"`{cmd}` exited {p.returncode}\n{tail}"}], meta
    return [], meta


def verify(charter_path: str, root: str, quiet: bool = False) -> dict:
    """Run all checks; return a report dict."""
    data = load_charter(charter_path)
    violations: list[dict] = []
    hashes: dict[str, str] = {}
    for d in data.get("deliverable", []):
        violations += _check_deliverable(d, root)
        pattern = d.get("path")
        if pattern:
            for m in sorted(_glob.glob(os.path.join(root, pattern), recursive=True)):
                if os.path.isfile(m):
                    hashes[os.path.relpath(m, root)] = _sha256(m)
    check_meta = []
    for c in data.get("check", []):
        v, meta = _run_check(c, root)
        violations += v
        check_meta.append(meta)
    report = {
        "ts": _now(),
        "charter": data.get("charter", {}).get("name", os.path.basename(charter_path)),
        "charter_file": charter_path,
        "ok": not violations,
        "violations": violations,
        "checks": check_meta,
        "deliverable_sha256": hashes,
    }
    if not quiet:
        _print_report(report)
    return report


def _print_report(report: dict) -> None:
    name = report["charter"]
    if report["ok"]:
        n = len(report["deliverable_sha256"])
        print(f"charter: OK — `{name}` satisfied ({n} deliverable file(s), "
              f"{len(report['checks'])} check(s))")
    else:
        print(f"charter: BREACH — `{name}` has {len(report['violations'])} violation(s):")
        for v in report["violations"]:
            first = v["detail"].splitlines()[0]
            print(f"  - [{v['kind']}] {v['deliverable']}: {first}")


def violations_markdown(report: dict) -> str:
    lines = [
        "# Charter violations",
        "",
        f"Contract `{report['charter']}` is NOT satisfied "
        f"({len(report['violations'])} violation(s)). Fix ALL of the following, "
        "then the contract will be re-verified:",
        "",
    ]
    for v in report["violations"]:
        lines.append(f"## [{v['kind']}] {v['deliverable']}")
        lines.append("```")
        lines.append(v["detail"])
        lines.append("```")
        lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------- audit

def _audit_append(root: str, record: dict) -> None:
    d = os.path.join(root, CHARTER_DIR)
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, AUDIT_FILE)
    # hash-chain: each record carries the sha256 of the previous line (tamper-evident)
    prev = "0" * 64
    if os.path.exists(path):
        with open(path, "rb") as f:
            lines = f.read().splitlines()
        if lines:
            prev = hashlib.sha256(lines[-1]).hexdigest()
    record = {"prev": prev, **record}
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, sort_keys=True) + "\n")


def cmd_log(root: str) -> int:
    path = os.path.join(root, CHARTER_DIR, AUDIT_FILE)
    if not os.path.exists(path):
        print("charter: no audit log yet")
        return 0
    ok = True
    prev = "0" * 64
    with open(path, "rb") as f:
        raw = f.read().splitlines()
    for i, line in enumerate(raw):
        rec = json.loads(line)
        if rec.get("prev") != prev:
            ok = False
            print(f"!! audit line {i + 1}: hash chain broken")
        prev = hashlib.sha256(line).hexdigest()
        verdict = "OK " if rec.get("ok") else "FAIL"
        print(f"{rec.get('ts','?')}  {verdict} event={rec.get('event','?')} "
              f"attempt={rec.get('attempt','-')} violations={len(rec.get('violations',[]))}")
    print(f"charter: audit chain {'intact' if ok else 'BROKEN'} ({len(raw)} record(s))")
    return 0 if ok else 1


# ----------------------------------------------------------------------- run

def cmd_run(charter_path: str, root: str, agent_cmd: list[str],
            max_repairs: int) -> int:
    """Run agent command, verify, repair-loop on breach."""
    viol_path = os.path.join(root, CHARTER_DIR, VIOLATIONS_FILE)
    os.makedirs(os.path.join(root, CHARTER_DIR), exist_ok=True)
    if os.path.exists(viol_path):
        os.remove(viol_path)

    attempts = max_repairs + 1
    report: dict = {}
    for attempt in range(1, attempts + 1):
        cmd = list(agent_cmd)
        # placeholder substitution so prompt-driven agents can receive the report
        if attempt > 1:
            vmd = violations_markdown(report)
            cmd = [a.replace("{violations}", vmd) for a in cmd]
        env = dict(os.environ,
                   CHARTER_ATTEMPT=str(attempt),
                   CHARTER_VIOLATIONS=viol_path if attempt > 1 else "")
        print(f"charter: attempt {attempt}/{attempts}: {shlex.join(agent_cmd)[:200]}",
              file=sys.stderr)
        p = subprocess.run(cmd, cwd=root, env=env)
        report = verify(charter_path, root)
        _audit_append(root, {
            "ts": _now(), "event": "run", "attempt": attempt,
            "agent_cmd": shlex.join(agent_cmd), "agent_exit": p.returncode,
            "ok": report["ok"], "violations": report["violations"],
            "deliverable_sha256": report["deliverable_sha256"],
        })
        if report["ok"]:
            if os.path.exists(viol_path):
                os.remove(viol_path)
            return 0
        with open(viol_path, "w", encoding="utf-8") as f:
            f.write(violations_markdown(report))
    print(f"charter: contract still breached after {attempts} attempt(s); "
          f"see {viol_path}", file=sys.stderr)
    return 1


# ---------------------------------------------------------------------- main

def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    # split off agent command after `--`
    agent_cmd: list[str] = []
    if "--" in argv:
        i = argv.index("--")
        agent_cmd = argv[i + 1:]
        argv = argv[:i]

    ap = argparse.ArgumentParser(prog="charter",
                                 description="Deliverable contracts for AI agents.")
    ap.add_argument("--version", action="version", version=f"charter {__version__}")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_init = sub.add_parser("init", help="scaffold a charter.toml")
    p_init.add_argument("-c", "--charter", default="charter.toml")

    for name in ("verify", "run"):
        p = sub.add_parser(name)
        p.add_argument("-c", "--charter", default="charter.toml")
        p.add_argument("-C", "--root", default=".", help="project root to verify in")
        p.add_argument("--json", action="store_true", help="print full JSON report")
        if name == "run":
            p.add_argument("--max-repairs", type=int, default=2)

    sub.add_parser("log", help="print + verify the audit trail").add_argument(
        "-C", "--root", default=".")

    args = ap.parse_args(argv)

    if args.cmd == "init":
        if os.path.exists(args.charter):
            print(f"charter: {args.charter} already exists; not overwriting")
            return 1
        with open(args.charter, "w", encoding="utf-8") as f:
            f.write(TEMPLATE)
        print(f"charter: wrote {args.charter}")
        return 0

    if args.cmd == "verify":
        report = verify(args.charter, args.root)
        _audit_append(args.root, {
            "ts": _now(), "event": "verify", "ok": report["ok"],
            "violations": report["violations"],
            "deliverable_sha256": report["deliverable_sha256"],
        })
        if args.json:
            print(json.dumps(report, indent=2))
        return 0 if report["ok"] else 1

    if args.cmd == "run":
        if not agent_cmd:
            ap.error("run requires an agent command after `--`")
        return cmd_run(args.charter, args.root, agent_cmd, args.max_repairs)

    if args.cmd == "log":
        return cmd_log(args.root)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
