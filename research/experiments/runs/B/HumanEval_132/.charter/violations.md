# Charter violations

Contract `humaneval-HumanEval_132` is NOT satisfied (1 violation(s)). Fix ALL of the following, then the contract will be re-verified:

## [check_failed] smoke-passes
```
`python3 smoke_test.py` exited 1
Traceback (most recent call last):
  File "/private/tmp/long-horizon-research/govern-deliverables-claude-fruitcake-eap[1m]-20260605T192155Z/experiments/runs/B/HumanEval_132/smoke_test.py", line 17, in <module>
    assert is_nested('[][][]') == False, "Failed: [][][]"
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Failed: [][][]
```
