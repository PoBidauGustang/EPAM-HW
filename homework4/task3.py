import sys


def my_precious_logger(text: str):
    if text.startswith("error"):
        sys.stderr.write(text)
    else:
        sys.stdout.write(text)
