#!/usr/bin/env python3
"""Score arm B's FIRST-ATTEMPT solutions (condition B0) with the official harness.

solution.py in runs/B/<task>/ is the post-repair file; the first attempt's raw
model output is preserved in call_1.txt. We re-extract solution.py from call_1.txt
with the same parsing logic as agent_driver.py, so B0 = "what B would have
delivered with no repair loop". B vs B0 isolates the verify->repair gate's effect
on hidden-test pass rate within arm B.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "vendor-human-eval"))
from human_eval.data import read_problems, write_jsonl  # noqa: E402
from human_eval.evaluation import evaluate_functional_correctness  # noqa: E402


def extract_solution(text: str) -> str | None:
    m = re.search(r"###\s*solution\.py\s*```(?:python)?\n(.*?)```", text, re.DOTALL)
    if m:
        return m.group(1)
    blocks = re.findall(r"```(?:python)?\n(.*?)```", text, re.DOTALL)
    return blocks[0] if blocks else None


def main() -> int:
    problems = read_problems()
    samples, missing = [], []
    for tid in problems:
        safe = tid.replace("/", "_")
        c1 = os.path.join(HERE, "runs", "B", safe, "call_1.txt")
        code = extract_solution(open(c1, encoding="utf-8", errors="replace").read()) \
            if os.path.exists(c1) else None
        if code is None:
            code = ""
            missing.append(tid)
        samples.append({"task_id": tid, "completion": "\n\n" + code})
    out = os.path.join(HERE, "runs", "samples_B0.jsonl")
    write_jsonl(out, samples)
    print(f"B0: {len(samples)} samples, {len(missing)} unparseable {missing[:5]}")
    res = evaluate_functional_correctness(out, k=[1], n_workers=8, timeout=10.0)
    print("B0", res)
    with open(os.path.join(HERE, "runs", "pass_at_1_B0.json"), "w") as fh:
        json.dump(res, fh, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
