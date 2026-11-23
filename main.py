"""Plan entry for the-plan-make-fun-will-carry-20261122-2138.

Writes one executable 30-day plan to /output/entry.txt: a single
reusable digital asset (an abandoned-cart email pack for Shopify
stores) sold to real store owners found in the open, at a real price,
on a real marketplace. No human labour, no stock, no luck.
"""

import os
import sys

PLAN = (
    "Day 1: build a $39 abandoned-cart email pack for Shopify stores"
    "\u20145 emails plus setup guide, tested on a free trial store. "
    "Days 2\u201330: find 200 stores via BuiltWith, pitch owners through "
    "contact forms, sell on Gumroad. 12 sales = $468. "
    "One asset reused; no stock, no ads, no luck."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    text = PLAN
    if not text.strip():
        print("plan is empty", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 280:
        print(f"plan is {len(text)} code points, must be 1-280", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    # Verify what landed on disk: read it back and compare byte for byte,
    # so a truncated or re-encoded write fails loudly instead of silently.
    with open(path, "rb") as handle:
        on_disk = handle.read()
    if on_disk != text.encode("utf-8"):
        print("entry.txt on disk does not match the plan", file=sys.stderr)
        return 1
    if not 1 <= len(on_disk.decode("utf-8")) <= 280:
        print("entry.txt length out of range after write", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(text)} code points)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
