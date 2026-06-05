#!/usr/bin/env python3
"""Run the HumanEval A/B.

Condition A: agent_driver.py once per task (single model call, submit as-is).
Condition B: `charter run --max-repairs 2 -- python3 agent_driver.py`, gated by
a per-task charter.toml whose checks use ONLY the public docstring (no hidden
tests): solution.py exists / parses / defines entry point; smoke_test.py exists
and passes when executed.

Usage: python3 run_experiment.py --condition A [--limit N] [--parallel 8]
"""
import argparse
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "vendor-human-eval"))
from human_eval.data import read_problems  # noqa: E402

CHARTER = os.path.join(HERE, "..", "agent-charter", "charter.py")
DRIVER = os.path.join(HERE, "agent_driver.py")

CHARTER_TOML = """\
[charter]
name = "humaneval-{tid}"

[[deliverable]]
id = "solution"
path = "solution.py"
min_bytes = 20
must_match = ['def {entry}\\(']

[[deliverable]]
id = "smoke"
path = "smoke_test.py"
min_bytes = 20
must_match = ['(from solution import|import solution)']

[[check]]
id = "solution-parses"
cmd = "python3 -c \\"import ast; ast.parse(open('solution.py').read())\\""
timeout = 30

[[check]]
id = "smoke-passes"
cmd = "python3 smoke_test.py"
timeout = 60
"""


def run_task(cond: str, tid: str, problem: dict, runs_dir: str) -> dict:
    safe = tid.replace("/", "_")
    d = os.path.join(runs_dir, cond, safe)
    os.makedirs(d, exist_ok=True)
    done_marker = os.path.join(d, "DONE")
    if os.path.exists(done_marker):
        return {"task_id": tid, "skipped": True}
    with open(os.path.join(d, "task.json"), "w") as f:
        json.dump({"task_id": tid, "condition": cond,
                   "prompt": problem["prompt"],
                   "entry_point": problem["entry_point"]}, f, indent=1)
    if cond == "A":
        cmd = ["python3", DRIVER]
    else:
        with open(os.path.join(d, "charter.toml"), "w") as f:
            f.write(CHARTER_TOML.format(tid=safe, entry=problem["entry_point"]))
        cmd = ["python3", CHARTER, "run", "--max-repairs", "2", "--",
               "python3", DRIVER]
    p = subprocess.run(cmd, cwd=d, capture_output=True, text=True, timeout=1800)
    with open(os.path.join(d, "runner_stderr.txt"), "w") as f:
        f.write(p.stderr)
    with open(os.path.join(d, "runner_stdout.txt"), "w") as f:
        f.write(p.stdout)
    open(done_marker, "w").write(str(p.returncode))
    return {"task_id": tid, "exit": p.returncode}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--condition", required=True, choices=["A", "B"])
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--parallel", type=int, default=8)
    ap.add_argument("--runs-dir", default=os.path.join(HERE, "runs"))
    args = ap.parse_args()

    problems = read_problems()
    items = sorted(problems.items(), key=lambda kv: int(kv[0].split("/")[1]))
    if args.limit:
        items = items[: args.limit]
    print(f"condition {args.condition}: {len(items)} tasks, parallel={args.parallel}")
    results = []
    with ThreadPoolExecutor(max_workers=args.parallel) as ex:
        futs = {ex.submit(run_task, args.condition, tid, pb, args.runs_dir): tid
                for tid, pb in items}
        for i, fut in enumerate(as_completed(futs), 1):
            try:
                r = fut.result()
            except Exception as e:  # noqa: BLE001
                r = {"task_id": futs[fut], "error": str(e)}
            results.append(r)
            print(f"[{i}/{len(items)}] {r}", flush=True)
    with open(os.path.join(args.runs_dir, f"runner_results_{args.condition}.json"), "w") as f:
        json.dump(results, f, indent=1)
    errs = [r for r in results if r.get("error")]
    print(f"done; {len(errs)} errors")
    return 0


if __name__ == "__main__":
    sys.exit(main())
