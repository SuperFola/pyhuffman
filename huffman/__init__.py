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


def encode_as_bytes(buffer: str, htree: tree.Tree, uses_n_bits: int = 8):
    buffer = encode(buffer, htree)

    bits = [buffer[0]]
    for i, c in enumerate(buffer[1:]):
        if (1 + i) % uses_n_bits == 0:
            bits.append(c)
        else:
            bits[-1] += c

    bits = [int(f"0b{b}", 2) for b in bits]
    return bits


def decode_from_bytes(buffer, htree: tree.Tree, uses_n_bit: int = 8):
    bits = [bin(c)[2:] for c in buffer]
    print(len(''.join(bits)))
    print(''.join(bits))
    return bits
