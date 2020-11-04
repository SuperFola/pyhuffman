#!/usr/bin/env python3

from . import coding, tree


def encode(buffer: str, htree: dict) -> str:
    return "".join(htree[c] for c in buffer)


def decode(buffer: str, htree: dict) -> str:
    code = {v: k for k, v in htree.items()}
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


def encode_as_bytes(buffer: str, htree: dict):
    buffer = encode(buffer, htree)

    bits = [buffer[0]]
    for i, c in enumerate(buffer[1:]):
        if (1 + i) % 7 == 0:
            bits.append(c)
        else:
            bits[-1] += c

    bits_to_int = [int(f"0b{b}", 2) for b in bits]
    last_byte_size = len(bits[-1])
    bits_to_int[-1:-1] = [last_byte_size]

    bits = bytes("".join(chr(b) for b in bits_to_int), encoding='ascii')
    return bits


def decode_from_bytes(buffer, htree: dict):
    bits = [ord(c) for c in buffer.decode('ascii')]
    last = bits.pop(-2)
    new_bits = [bin(b)[2:].zfill(7) for b in bits[:-1]]
    new_bits.append(bin(bits[-1])[2:].zfill(last))

    return decode("".join(new_bits), htree)
