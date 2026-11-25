"""Write a hurried GTA 6 launch-week absence text to entry.txt.
The boiler appointment keeps the excuse mundane, with launch timing as the twist.
"""

import os
from pathlib import Path


LINE = "The boiler guy can only come Thursday, launch day."


def validate() -> None:
    data = (Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output") / "entry.txt").read_bytes()
    text = data.decode("utf-8")
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert len(text.split()) <= 20, "entry must be at most 20 words"
    assert text == text.strip(), "no leading/trailing whitespace"
    assert "\n" not in text, "single line only"
    assert not data.endswith(b"\n"), "no trailing newline"


def main() -> None:
    if not LINE.strip():
        raise ValueError("The entry line must not be empty or whitespace-only.")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))
    validate()


if __name__ == "__main__":
    main()
