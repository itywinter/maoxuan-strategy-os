# Maoxuan Strategy OS

A portable Agent Skill for evidence-based strategic reasoning. It combines the methodological discipline of **实事求是、调查研究、具体问题具体分析、抓重点、集中力量、实践检验、根据新情况修正认识** with modern problem structuring, decision science, systems thinking, experimentation, and strategy tools.

## What it is

This is not a Mao quotation bot and not historical role-play. It is a decision operating system for messy real-world problems where facts, hypotheses, stakeholders, constraints, timing, and resource allocation interact.

## Installation

The portable skill is the `maoxuan-strategy-os/` directory itself. For current Codex managed skill installation, place/copy the directory under `$CODEX_HOME/skills/` (commonly `~/.codex/skills/`) or install it from a GitHub repository through the skill installer. Restart/reload Codex if required by your client.

## Use examples

- “公司收入下降，到底是市场、产品还是销售？”
- “为什么这个政府项目最后没有推进？现在还值得追吗？”
- “现金只有 8 个月，现金是不是主要矛盾？”
- “我们是小公司，怎么和大型 incumbent 竞争？”
- “Pilot 技术成功但客户不付款，要不要继续？”
- “三个职业选择各有代价，怎么把事实和价值分开？”

## Design philosophy

1. **Reality before framework.**
2. **Minimum sufficient reasoning.** Use only the methods that improve the next decision.
3. **No analytical immunity.** Authority and confidence are not evidence.
4. **No forced certainty.** Evidence gaps stay visible.
5. **Strategy must move resources.** A stated priority with no resource change is not a real priority.
6. **Practice closes the loop.** Results must be allowed to revise the model.

## Structure

- `SKILL.md` — compact operating instructions and router
- `references/constitution/` — objectivity and dialogue constitution
- `references/gates/` — seven system gates
- `references/truth/` — problem framing, investigation, hypotheses, historical reconstruction
- `references/strategy/` — contradiction, stage, options, focus
- `references/action/` — experiments, failure classification, review
- `references/decision-tools/` — reversibility, incentive analysis, value of information
- `references/knowledge/` — methodology/source map
- `references/tests/` — regression and adversarial tests
- `scripts/validate_skill.py` — local structural validator

## Important boundary

This skill improves decision quality; it does not replace domain specialists for legal, medical, engineering-safety, accounting, tax, or regulatory sign-off.
