#!/usr/bin/env python3
"""Paired analysis of the A/B. Reads ONLY committed artifacts:
  runs/samples_{A,B}.jsonl_results.jsonl  (official human-eval per-task verdicts)
  runs/{A,B}/<task>/meta.json             (model-call counts/latency)
  runs/B/<task>/.charter/audit.jsonl      (charter attempts/verdicts)
Writes results.json (consumed by the paper) and prints a summary.
"""
import glob
import json
import math
import os
from scipy.stats import binomtest

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = os.path.join(HERE, "runs")


def load_results(cond: str) -> dict[str, bool]:
    path = os.path.join(RUNS, f"samples_{cond}.jsonl_results.jsonl")
    out = {}
    for line in open(path):
        r = json.loads(line)
        out[r["task_id"]] = r["passed"]
    return out


def wilson(p: float, n: int, z: float = 1.96) -> tuple[float, float]:
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return c - h, c + h


def main() -> None:
    a, b = load_results("A"), load_results("B")
    tasks = sorted(a, key=lambda t: int(t.split("/")[1]))
    assert set(a) == set(b) and len(tasks) == 164, (len(a), len(b))

    pa = sum(a.values()) / len(tasks)
    pb = sum(b.values()) / len(tasks)
    b01 = sum(1 for t in tasks if not a[t] and b[t])  # B fixed
    b10 = sum(1 for t in tasks if a[t] and not b[t])  # B broke
    # exact McNemar: binomial test on discordant pairs
    n_disc = b01 + b10
    mcnemar_p = binomtest(b01, n_disc, 0.5).pvalue if n_disc else 1.0

    # call/latency stats per condition
    stats = {}
    for cond in ("A", "B"):
        calls, secs = [], []
        for mp in glob.glob(os.path.join(glob.escape(RUNS), cond, "*", "meta.json")):
            m = json.load(open(mp))
            calls.append(len(m["calls"]))
            secs.append(sum(c["seconds"] for c in m["calls"]))
        stats[cond] = {
            "n_tasks_with_meta": len(calls),
            "mean_model_calls": sum(calls) / len(calls),
            "total_model_calls": sum(calls),
            "mean_model_seconds": sum(secs) / len(secs),
        }

    # charter audit stats for B
    first_pass = repaired = unresolved = 0
    repaired_tasks: list[str] = []
    unresolved_tasks: list[str] = []
    attempts_hist: dict[int, int] = {}
    for ap in glob.glob(os.path.join(glob.escape(RUNS), "B", "*", ".charter", "audit.jsonl")):
        recs = [json.loads(l) for l in open(ap)]
        runs = [r for r in recs if r["event"] == "run"]
        n_att = max(r["attempt"] for r in runs)
        attempts_hist[n_att] = attempts_hist.get(n_att, 0) + 1
        final_ok = runs[-1]["ok"]
        tid = "HumanEval/" + os.path.basename(os.path.dirname(os.path.dirname(ap))).split("_")[1]
        if n_att == 1 and final_ok:
            first_pass += 1
        elif final_ok:
            repaired += 1
            repaired_tasks.append(tid)
        else:
            unresolved += 1
            unresolved_tasks.append(tid)

    # B0 = arm B first attempts (no repair loop), if scored
    b0_path = os.path.join(RUNS, "samples_B0.jsonl_results.jsonl")
    b0_block = None
    if os.path.exists(b0_path):
        b0 = load_results("B0")
        pb0 = sum(b0.values()) / len(tasks)
        b0_block = {
            "pass_at_1_B0": pb0, "passed_B0": sum(b0.values()),
            "repair_fixed_hidden": [t for t in tasks if not b0[t] and b[t]],
            "repair_broke_hidden": [t for t in tasks if b0[t] and not b[t]],
            # among contract-repaired tasks: how many first attempts already
            # passed hidden tests (=> smoke-test false alarm) vs not (true bug)
            "repaired_tasks": sorted(repaired_tasks),
            "repaired_false_alarm": sum(1 for t in repaired_tasks if b0[t]),
            "repaired_true_bug": sum(1 for t in repaired_tasks if not b0[t]),
            "unresolved_tasks": unresolved_tasks,
            "unresolved_hidden_pass": sum(1 for t in unresolved_tasks if b[t]),
        }

    res = {
        "n_tasks": len(tasks),
        "pass_at_1_A": pa, "pass_at_1_B": pb,
        "passed_A": sum(a.values()), "passed_B": sum(b.values()),
        "wilson95_A": wilson(pa, len(tasks)), "wilson95_B": wilson(pb, len(tasks)),
        "delta_pp": (pb - pa) * 100,
        "discordant_B_fixed": b01, "discordant_B_broke": b10,
        "mcnemar_exact_p": mcnemar_p,
        "call_stats": stats,
        "charter_B": {"first_attempt_ok": first_pass, "repaired_to_ok": repaired,
                      "unresolved_breach": unresolved,
                      "attempts_histogram": attempts_hist},
        "fixed_tasks": [t for t in tasks if not a[t] and b[t]],
        "broken_tasks": [t for t in tasks if a[t] and not b[t]],
        "B0_first_attempt": b0_block,
    }
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(res, f, indent=1)
    print(json.dumps(res, indent=1))

    # LaTeX macros for the paper: every number in the paper comes from here.
    def pct(x: float) -> str:
        return f"{100 * x:.1f}"

    macros = {
        "ntasks": str(len(tasks)),
        "passA": str(res["passed_A"]), "passB": str(res["passed_B"]),
        "pAa": pct(pa), "pBb": pct(pb),
        "ciAlo": pct(res["wilson95_A"][0]), "ciAhi": pct(res["wilson95_A"][1]),
        "ciBlo": pct(res["wilson95_B"][0]), "ciBhi": pct(res["wilson95_B"][1]),
        "deltapp": f"{res['delta_pp']:.1f}",
        "bfixed": str(b01), "bbroke": str(b10),
        "mcnemarp": f"{mcnemar_p:.4f}" if mcnemar_p >= 1e-4 else f"{mcnemar_p:.1e}",
        "meancallsA": f"{stats['A']['mean_model_calls']:.2f}",
        "meancallsB": f"{stats['B']['mean_model_calls']:.2f}",
        "meansecsA": f"{stats['A']['mean_model_seconds']:.1f}",
        "meansecsB": f"{stats['B']['mean_model_seconds']:.1f}",
        "totalcallsB": str(stats["B"]["total_model_calls"]),
        "firstpassB": str(first_pass), "repairedB": str(repaired),
        "unresolvedB": str(unresolved),
    }
    if b0_block:
        macros.update({
            "pBz": pct(b0_block["pass_at_1_B0"]),
            "passBz": str(b0_block["passed_B0"]),
            "repairfixedhidden": str(len(b0_block["repair_fixed_hidden"])),
            "repairbrokehidden": str(len(b0_block["repair_broke_hidden"])),
            "repairedfalsealarm": str(b0_block["repaired_false_alarm"]),
            "repairedtruebug": str(b0_block["repaired_true_bug"]),
            "unresolvedhiddenpass": str(b0_block["unresolved_hidden_pass"]),
        })
    with open(os.path.join(HERE, "..", "paper", "numbers.tex"), "w") as f:
        f.write("% AUTO-GENERATED by experiments/analyze.py from committed raw logs. Do not edit.\n")
        for k, v in macros.items():
            f.write(f"\\newcommand{{\\num{k}}}{{{v}}}\n")


if __name__ == "__main__":
    main()
