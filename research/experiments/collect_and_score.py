#!/usr/bin/env python3
"""Collect solutions from runs/{A,B} into samples_{A,B}.jsonl and score them
with the OFFICIAL human-eval harness (vendored, unmodified, commit 6d43fb9).

completion := "\n\n" + full solution file. Appending a complete top-level
redefinition after the benchmark prompt is valid Python (the prompt's stub body
is its docstring) and is scored by the official check program on entry_point.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "vendor-human-eval"))
from human_eval.data import read_problems, write_jsonl  # noqa: E402
from human_eval.evaluation import evaluate_functional_correctness  # noqa: E402


def collect(cond: str) -> str:
    problems = read_problems()
    samples = []
    missing = []
    for tid in problems:
        safe = tid.replace("/", "_")
        sol = os.path.join(HERE, "runs", cond, safe, "solution.py")
        if os.path.exists(sol):
            code = open(sol, encoding="utf-8", errors="replace").read()
        else:
            code = ""
            missing.append(tid)
        samples.append({"task_id": tid, "completion": "\n\n" + code})
    out = os.path.join(HERE, "runs", f"samples_{cond}.jsonl")
    write_jsonl(out, samples)
    print(f"{cond}: {len(samples)} samples, {len(missing)} missing solution files {missing[:5]}")
    return out


def main() -> int:
    for cond in ("A", "B"):
        f = collect(cond)
        res = evaluate_functional_correctness(f, k=[1], n_workers=8, timeout=10.0)
        print(cond, res)
        with open(os.path.join(HERE, "runs", f"pass_at_1_{cond}.json"), "w") as fh:
            json.dump(res, fh, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
