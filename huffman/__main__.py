#!/usr/bin/env python3

import sys

from . import coding, decode, encode, tree, encode_as_bytes, decode_from_bytes


def main(display_tree: bool, display_code:bool, encode_decode: bool, *args):
    text = " ".join(args)
    out = tree.from_string(text)

    if display_tree:
        print(out)
        print(f"depth: {out.depth}")
    if display_code:
        print(coding.generate(out))
    if encode_decode:
        print(f"Base text: '{text}', number of bits needed: {len(text) * 8}")
        e = encode(text, coding.generate(out))
        print(f"Encoded text: '{e}', numbers of bits needed: {len(e)}")
        d = decode(e, coding.generate(out))
        print(f"Decoded text: '{d}'")

        eb = encode_as_bytes(text, coding.generate(out))
        print(eb)
        db = decode_from_bytes(eb, coding.generate(out))
        print(db)


if __name__ == "__main__":
    args = sys.argv[1:]

    display_tree = args[0] == "-t"
    if display_tree:
        args.pop(0)

    display_code = args[0] == "-c"
    if display_code:
        args.pop(0)

    encode_decode = args[0] == "-e"
    if encode_decode:
        args.pop(0)

    main(
        display_tree,
        display_code,
        encode_decode,
        *args,
    )
