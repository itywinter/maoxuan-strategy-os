# Failure Classification

## Purpose

After a failed attempt, identify **where the failure occurred** before deciding whether to continue, modify, or stop.

## Failure locations

- problem thesis — the problem is not real/important
- market — demand or buying behavior is insufficient
- business model — value cannot be captured economically
- architecture — core technical/business structure is not viable
- design — a specific design choice failed
- execution — viable plan was executed badly
- process — testing, QA, governance, or coordination system failed
- resource — the attempt was not adequately resourced
- timing — right idea at the wrong time/window
- learning — failure occurred but the mechanism remains unknown

## Decision sequence

1. Did the failure falsify the core thesis?
   - yes → change strategy / stop
2. If not, is there a specific evidence-backed corrective hypothesis?
   - no → pause and investigate
3. Can the next action validly test that corrective hypothesis?
   - yes → continue as a falsification test, not an act of faith

## Anti-excuse rule

Do not automatically say “strategy was right, execution was poor”. Require evidence that competent execution would plausibly change the outcome.

## Persistence test

Persistence = new evidence → changed understanding → changed action → new test.

Same belief + same action + explanations for every bad result = escalation of commitment.
