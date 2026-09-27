# Installation

## Codex managed skills

Copy the entire `maoxuan-strategy-os` directory into:

```text
$CODEX_HOME/skills/maoxuan-strategy-os
```

When `CODEX_HOME` is not set, the managed installer commonly uses:

```text
~/.codex/skills/maoxuan-strategy-os
```

Reload/restart the Codex client if it does not discover the skill immediately.

## Git repository installation

If you publish this directory to GitHub, Codex's skill installer can install a skill from a repository path/URL. Keep the directory name identical to the frontmatter `name` (`maoxuan-strategy-os`).

## Other Agent Skills-compatible clients

The package follows the portable Agent Skills convention: a skill directory containing a required `SKILL.md`, with supporting material under `references/` and deterministic helpers under `scripts/`. Exact discovery/install paths vary by client.

## Validate locally

From the skill directory:

```bash
python scripts/validate_skill.py
```

Expected output begins with:

```text
VALIDATION PASSED
```
