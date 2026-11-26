"""The Internet in One Word.

The entry is a single word, written to /output/entry.txt and nothing else.
"""

import os

# One word, seven letters: the whole internet, still talking.
WORD = "yapping"


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 30 characters,
    # a single word and nothing else.
    assert 1 <= len(WORD) <= 30, "entry word must be 1 to 30 characters"
    assert WORD.split() == [WORD], "entry must be exactly one word"
    output = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(output)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
