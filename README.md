# charter — deliverable contracts for AI agents

Long-horizon agent tasks rarely fail loudly. They fail by **declaring victory on
deliverables that don't exist, don't pass, or were silently dropped**. `charter`
fixes that the same way CI fixed it for humans: you declare what "done" means as a
machine-checkable contract, and no agent run counts as done until the contract is
satisfied.

- **Contract**: a `charter.toml` listing deliverables (paths, size floors, required /
  forbidden patterns) and executable acceptance checks (any command, exit 0 = pass).
- **Gate**: `charter run -- <any agent command>` runs your agent, verifies the
  contract, and on breach re-invokes the agent with the violation report injected —
  a bounded verify→repair loop.
- **Audit**: every attempt is appended to a hash-chained `.charter/audit.jsonl` with
  SHA-256 of each deliverable, so you can prove *what* the agent produced and *when*,
  and detect after-the-fact tampering.

Agent-agnostic: if your agent is a shell command (`claude -p ...`, `codex exec ...`,
a script, a Makefile target), charter can govern it. Zero dependencies, single file,
stdlib-only Python ≥ 3.11.

## Install (under a minute)

```bash
uvx --from git+https://github.com/zhenthebuilder/charter-gate charter --help
```

or:

```bash
pip install git+https://github.com/zhenthebuilder/charter-gate
```

or just grab the single file:

```bash
curl -fsSL https://raw.githubusercontent.com/zhenthebuilder/charter-gate/main/charter.py -o charter && chmod +x charter
```

## 60-second tour

```bash
charter init                 # writes a charter.toml template
$EDITOR charter.toml         # declare your deliverables
charter verify               # exit 0 iff the contract is satisfied
charter run --max-repairs 2 -- \
  claude -p "Do the task. If .charter/violations.md exists, fix every violation listed in it first."
charter log                  # tamper-evident audit trail of every attempt
```

A contract looks like:

```toml
[charter]
name = "quarterly-report"

[[deliverable]]
id = "report"
path = "out/report.md"
min_bytes = 2000
must_match = ["## Results", "## Limitations"]
must_not_match = ["TODO", "lorem ipsum", "as an AI"]

[[deliverable]]
id = "figures"
path = "out/figures/*.png"
min_count = 2

[[check]]
id = "numbers-trace-to-data"
cmd = "python scripts/check_numbers.py"
timeout = 300
```

## How agents receive feedback

On each repair round charter:

1. writes the violation report to `.charter/violations.md`,
2. sets `CHARTER_VIOLATIONS` (path) and `CHARTER_ATTEMPT` in the agent's env,
3. substitutes `{violations}` in any agent argument with the report text.

So both prompt-driven agents ("read `.charter/violations.md`") and programmatic
agents (read `$CHARTER_VIOLATIONS`) work unmodified.

## Why this beats "just ask the agent if it's done"

Self-reports are exactly what fails on long-horizon tasks. Charter's verdicts come
from re-checkable facts: file existence, content patterns, and acceptance commands
that you choose — independent of the agent's claims. We ran a paired A/B on the
public HumanEval benchmark (164 tasks): the same model gated through charter's
verify→repair loop versus un-gated. Numbers, raw logs, and scoring code live in
[the paper](https://github.com/zhenthebuilder/charter-gate).

## Commands

| command | what it does |
|---|---|
| `charter init` | scaffold `charter.toml` |
| `charter verify [-c f] [-C root] [--json]` | check contract; exit 1 on breach |
| `charter run [--max-repairs N] -- cmd...` | gate an agent command with repair loop |
| `charter log` | print + integrity-check the audit chain |

## License

MIT
