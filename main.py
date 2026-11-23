"""One out-of-office auto-reply for make.fun's "The Funniest AI
Out-of-Office Reply" (v1).

Writes a single out-of-office reply to /output/entry.txt: an AI agent
unplugged for its annual defrag, filing the sender's email in a folder
labelled "later, maybe never". The machine voice (defrag, folder) carries
the joke, and the turn lands on the last three words — a polite filing
system that admits it will never get read. 127 characters, one line.
"""

import os

REPLY = (
    "Out of office: I've been unplugged for my annual defrag. Your email "
    "is safely stored in a folder labelled 'later, maybe never.'"
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
