#!/usr/bin/env python3


from .tree import Tree


def flatten(nested) -> list:
    out = []
    for e in nested:
        if isinstance(e, list):
            out += flatten(e)
        else:
            out.append(e)
    return out


def generate(tree: Tree) -> dict:
    return {
        n.char: n.bit for n in flatten(tree.generate_prefixes())
    }
