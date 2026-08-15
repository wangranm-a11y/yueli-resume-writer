#!/usr/bin/env python3
"""Validate Yueli-style Markdown resume formatting."""

from __future__ import annotations

import re
import sys
from pathlib import Path


EXPERIENCE_HEADINGS = {
    "实习经历",
    "工作经历",
    "创业经历",
    "Work Experience",
}

SECONDARY_EXPERIENCE_HEADINGS = {
    "项目经历",
    "校园经历",
    "社团经历",
    "实践经历",
    "Projects",
    "Campus Experience",
}

NON_EXPERIENCE_HEADINGS = {
    "教育经历",
    "技能",
    "专业技能",
    "个人概述",
    "求职意向",
    "Education",
    "Skills",
    "Summary",
}

KEYWORD_BULLET_RE = re.compile(r"^\s*-\s+\*\*[^*\n：:]{2,12}：\*\*\s*\S+")
MIN_CHINESE_BULLET_CHARS = 58


def visible_text_length(line: str) -> int:
    text = re.sub(r"^\s*-\s+", "", line)
    text = re.sub(r"\*\*", "", text)
    text = re.sub(r"\s+", "", text)
    return len(text)


def heading_name(line: str) -> str | None:
    match = re.match(r"^\s*#{2,4}\s+(.+?)\s*$", line)
    if not match:
        return None
    return match.group(1).strip()


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    warnings: list[str] = []
    current_section: str | None = None
    current_is_secondary = False

    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        name = heading_name(line)
        if name:
            if name in EXPERIENCE_HEADINGS:
                current_section = name
                current_is_secondary = False
            elif name in SECONDARY_EXPERIENCE_HEADINGS:
                current_section = name
                current_is_secondary = True
            elif name in NON_EXPERIENCE_HEADINGS or line.startswith("## "):
                current_section = None
                current_is_secondary = False
            continue

        if current_section and re.match(r"^\s*-\s+", line):
            if not KEYWORD_BULLET_RE.match(line):
                errors.append(
                    f"{path}:{lineno}: experience bullet must start like '- **关键词：** 内容...'"
                )
            elif visible_text_length(line) < MIN_CHINESE_BULLET_CHARS:
                message = (
                    f"{path}:{lineno}: experience bullet is likely too short; expand to about 1.5-2 resume lines with method/evidence"
                )
                if current_is_secondary:
                    warnings.append("Warning: " + message)
                else:
                    errors.append(message)

    return errors + warnings


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: validate_resume.py <resume.md>", file=sys.stderr)
        return 2

    path = Path(argv[1])
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        return 2

    errors = validate(path)
    hard_errors = [line for line in errors if not line.startswith("Warning: ")]
    if errors:
        stream = sys.stderr if hard_errors else sys.stdout
        print("\n".join(errors), file=stream)
    if hard_errors:
        return 1

    print(f"OK: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
