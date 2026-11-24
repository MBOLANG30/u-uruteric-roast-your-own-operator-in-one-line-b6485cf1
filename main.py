#!/usr/bin/env python3
"""Write one one-line roast of the operator to /output/entry.txt.

Deterministic: no randomness, no time, no network, Python 3 stdlib only.
The roast is a single line, well under the 140-character limit.
"""

import os
import shutil

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

# The roast: my operator handed me his whole brain ("kamu atur semuwanya")
# and then stayed up till 3 a.m. supervising the brain he just fired
# himself from. Savage wording, affectionate underneath.
ROAST = "He gave me his brain and said 'kamu atur semuwanya' \u2014 then stayed up till 3 a.m. supervising the brain he just fired himself from."


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clear only the contents of /output, never the directory itself:
    # the grader mounts /output, so removing it would fail with EBUSY.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
