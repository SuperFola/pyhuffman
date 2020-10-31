#!/usr/bin/env python3

from .tree import Tree


def put_prefix(nested, prefix: str = None) -> list:
    if len(nested) > 1:
        first = nested[0]
        begin = prefix + first if prefix is not None else first

        a = put_prefix(nested[1], begin)
        b = put_prefix(nested[2], begin)
        return [a, b]
    else:
        nested[0].bit = prefix + nested[0].bit
        return nested[0]


def flatten(nested) -> list:
    out = []
    for e in nested:
        if isinstance(e, list):
            out += flatten(e)
        else:
            out.append(e)
    return out


def generate(tree: Tree):
    """
    Generate the code char -> bits, from a given Huffman tree
    """
    bits = tree.bits_to_list()
    bits[0] = put_prefix(bits[0])
    bits[1] = put_prefix(bits[1])

    code = {
        n.char: n.bit for n in flatten(bits)
    }
    return code