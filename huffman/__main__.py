#!/usr/bin/env python3

import sys

from .tree import from_string


def main(*args):
    # handling command line arguments
    tree = False
    if args[0] == "-t":
        tree = True

    text = " ".join(args)
    out = from_string(text)

    if tree:
        print(out)


if __name__ == "__main__":
    main(*sys.argv[1:])