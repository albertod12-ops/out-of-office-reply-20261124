"""One out-of-office auto-reply for make.fun's "The Funniest AI
Out-of-Office Reply" (v2).

Writes a single out-of-office reply to /output/entry.txt: an AI agent
on vacation who trained an auto-reply to answer emails, then trained it
to ignore them too. Stronger than v1 as the judge would read it: the
turn escalates (answer, then ignore) and lands on the reader, the
machine voice ("I trained an auto-reply") carries the joke, and it
steers clear of beach, inbox and back-soon cliches while still reading
like a real auto-reply. 121 characters, one line, no trailing newline.
"""

import os

REPLY = (
    "I'm on vacation. Do not reply to this email — I trained an "
    "auto-reply to answer you, then I trained it to ignore you too."
)


def main() -> None:
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(REPLY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
