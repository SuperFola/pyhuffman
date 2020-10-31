#!/usr/bin/env python3

import sys

from .tree import min_weight, Node, Tree


def main(*args):
    # handling command line arguments
    tree = False
    if args[0] == "-t":
        tree = True

    text = " ".join(args)
    occurences = {}
    for e in text:
        if e not in occurences:
            occurences[e] = 1
        else:
            occurences[e] += 1
    occurences = sorted(
        list(Node(c, w) for c, w in occurences.items()),
        key=lambda n: n.w
    )

    out = Tree.from_list(occurences)
    if tree:
        print(out)


if __name__ == "__main__":
    main(*sys.argv[1:])