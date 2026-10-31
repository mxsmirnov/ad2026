#!/usr/bin/env python3
"""Следующий четырёхзначный номер ADR по файлам adr-NNNN-*.md."""

from pathlib import Path
import re
import sys

PATTERN = re.compile(r"^adr-(\d{4})-.+\.md$")
adr_dir = Path(sys.argv[1] if len(sys.argv) > 1 else "adr")
adr_dir.mkdir(parents=True, exist_ok=True)

numbers = []
for path in adr_dir.iterdir():
    if path.is_file():
        match = PATTERN.fullmatch(path.name)
        if match:
            numbers.append(int(match.group(1)))

next_number = max(numbers, default=0) + 1
if next_number > 9999:
    raise SystemExit("Невозможно назначить четырёхзначный номер ADR: диапазон исчерпан")
print(f"{next_number:04d}")
