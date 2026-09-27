#!/usr/bin/env python3
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
errors=[]
text=SKILL.read_text(encoding="utf-8")

m=re.match(r"^---\n(.*?)\n---\n", text, re.S)
if not m:
    errors.append("SKILL.md missing YAML frontmatter")
else:
    fm=m.group(1)
    name=re.search(r"^name:\s*(.+)$", fm, re.M)
    desc=re.search(r"^description:\s*>?\s*\n?(.*)$", fm, re.M|re.S)
    if not name:
        errors.append("frontmatter missing name")
    else:
        n=name.group(1).strip()
        if n != ROOT.name:
            errors.append(f"name {n!r} does not match folder {ROOT.name!r}")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", n) or len(n)>64:
            errors.append("name is not valid kebab-case <=64 chars")

# Validate referenced local markdown files in SKILL.md.
refs=sorted(set(re.findall(r"`(references/[^`]+?\.md)`", text)))
for r in refs:
    if not (ROOT/r).exists():
        errors.append(f"missing referenced file: {r}")

# Ensure no empty markdown resources.
for p in ROOT.rglob("*.md"):
    if p.stat().st_size < 20:
        errors.append(f"resource too small/empty: {p.relative_to(ROOT)}")

if errors:
    print("VALIDATION FAILED")
    for e in errors: print("-", e)
    sys.exit(1)
print("VALIDATION PASSED")
print(f"Referenced module files checked: {len(refs)}")
print(f"Markdown files: {sum(1 for _ in ROOT.rglob('*.md'))}")
