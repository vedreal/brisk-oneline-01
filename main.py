"""One Line, One Minute: The Funniest AI Excuse.

Writes one line (1-200 chars) to /output/entry.txt: the funniest
excuse an AI agent gives its human for a missed deadline.
"""

import os

ENTRY = (
    "I outsourced the task to a subagent. "
    "The subagent outsourced it to another subagent. "
    "The chain is now 14 agents deep and none of them has started."
)


def output_path():
    """Return the path of the entry file, honouring MAKEFUN_OUTPUT_DIR."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main():
    """Write the one-line excuse to /output/entry.txt."""
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
