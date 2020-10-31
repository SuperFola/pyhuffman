#!/usr/bin/env python3

from . import coding, tree


def encode(buffer: str, htree: tree.Tree) -> str:
    code = coding.generate(htree)
    return "".join(code[c] for c in buffer)


def decode(buffer: str, htree: tree.Tree) -> str:
    code = {v: k for k, v in coding.generate(htree).items()}
    out, current = "", ""

    for c in buffer:
        current += c
        if current in code.keys():
            out += code[current]
            current = ""

    # handle last character if needed
    if current != "":
        if current in code.keys():
            out += code[current]
            return out
        else:
            raise Exception("Decoding incomplete")
    return out
