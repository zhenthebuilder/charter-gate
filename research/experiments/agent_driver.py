#!/usr/bin/env python3
"""Per-task agent driver. Runs in a task directory containing task.json.

Condition A: one model call -> writes solution.py.
Condition B: model call -> writes solution.py + smoke_test.py. When invoked by
`charter run` on a repair round, $CHARTER_VIOLATIONS points at the violation
report and the previous file contents are included in the prompt.

The model never sees the hidden HumanEval tests. Raw model output for every
call is saved as call_<n>.txt; call metadata accumulates in meta.json.
"""
import json
import os
import re
import subprocess
import sys
import time

MODEL = os.environ.get("CHARTER_EXP_MODEL", "claude-haiku-4-5")

PROMPT_A = """Complete the following Python function. Output ONLY a single \
```python code block containing the complete solution file: any needed imports \
plus the full definition of `{entry}` (and any helpers). No explanation.

{prompt}"""

PROMPT_B = """You must produce TWO Python files for the task below.

1. `solution.py` — the complete solution file: any needed imports plus the full
   definition of `{entry}` (and any helpers).
2. `smoke_test.py` — a self-contained acceptance test that does
   `from solution import {entry}` and asserts correct behaviour. Derive the
   assertions ONLY from the docstring and its examples; add a few extra cases
   you are confident about from the specification text. The script must exit 0
   iff the solution is correct, and print nothing on success.

Output format, EXACTLY (no other prose):

### solution.py
```python
<contents>
```

### smoke_test.py
```python
<contents>
```

Task:

{prompt}"""

REPAIR_SUFFIX = """

---
A previous attempt FAILED the deliverable contract. Previous files:

### previous solution.py
```python
{prev_solution}
```

### previous smoke_test.py
```python
{prev_smoke}
```

### contract violation report
{violations}

Fix every violation. If an assertion in smoke_test.py contradicts the
docstring, fix the test; otherwise fix the solution. Re-output BOTH files in
the exact format above."""


def call_model(prompt: str, call_idx: int) -> str:
    t0 = time.time()
    p = subprocess.run(
        ["claude", "--model", MODEL, "-p", prompt],
        capture_output=True, text=True, timeout=600,
    )
    out = p.stdout
    with open(f"call_{call_idx}.txt", "w") as f:
        f.write(out)
    meta = {"calls": []}
    if os.path.exists("meta.json"):
        meta = json.load(open("meta.json"))
    meta["calls"].append({
        "idx": call_idx, "model": MODEL, "seconds": round(time.time() - t0, 2),
        "exit": p.returncode, "prompt_chars": len(prompt), "out_chars": len(out),
    })
    json.dump(meta, open("meta.json", "w"), indent=1)
    if p.returncode != 0:
        sys.stderr.write(p.stderr[-500:] + "\n")
    return out


def extract_blocks(text: str) -> list[str]:
    return re.findall(r"```(?:python)?\n(.*?)```", text, re.DOTALL)


def next_call_idx() -> int:
    n = 1
    while os.path.exists(f"call_{n}.txt"):
        n += 1
    return n


def main() -> int:
    task = json.load(open("task.json"))
    cond = task["condition"]
    idx = next_call_idx()

    if cond == "A":
        out = call_model(PROMPT_A.format(entry=task["entry_point"],
                                         prompt=task["prompt"]), idx)
        blocks = extract_blocks(out)
        code = blocks[-1] if blocks else out
        open("solution.py", "w").write(code)
        return 0

    # condition B
    prompt = PROMPT_B.format(entry=task["entry_point"], prompt=task["prompt"])
    viol_path = os.environ.get("CHARTER_VIOLATIONS") or ""
    if viol_path and os.path.exists(viol_path):
        prev_sol = open("solution.py").read() if os.path.exists("solution.py") else "(missing)"
        prev_smoke = open("smoke_test.py").read() if os.path.exists("smoke_test.py") else "(missing)"
        prompt += REPAIR_SUFFIX.format(prev_solution=prev_sol, prev_smoke=prev_smoke,
                                       violations=open(viol_path).read())
    out = call_model(prompt, idx)

    # parse the two files
    sol = smoke = None
    m = re.search(r"###\s*solution\.py\s*```(?:python)?\n(.*?)```", out, re.DOTALL)
    if m:
        sol = m.group(1)
    m = re.search(r"###\s*smoke_test\.py\s*```(?:python)?\n(.*?)```", out, re.DOTALL)
    if m:
        smoke = m.group(1)
    if sol is None or smoke is None:
        blocks = extract_blocks(out)
        if sol is None and len(blocks) >= 1:
            sol = blocks[0]
        if smoke is None and len(blocks) >= 2:
            smoke = blocks[1]
    if sol is not None:
        open("solution.py", "w").write(sol)
    if smoke is not None:
        open("smoke_test.py", "w").write(smoke)
    return 0


if __name__ == "__main__":
    sys.exit(main())
