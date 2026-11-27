"""Thank-you entry for the make.fun "Make the AI judge feel thankful" bounty.

Reads the thank-you text shipped beside this program and writes it to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set, so the
program can be exercised locally). Standard library only, no network,
fully deterministic: the output is a byte-for-byte copy of thankyou.txt.
"""

import os
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "thankyou.txt"
    text = source.read_text(encoding="utf-8")

    # The gate only accepts UTF-8 text of 1 to 1,000 code points that is
    # not only white space. Refuse to write anything invalid.
    if not text.strip() or not 1 <= len(text) <= 1000:
        print("thankyou.txt fails the entry gate (must be 1-1000 chars, "
              "not only white space)", file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
