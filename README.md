# Huffman

Implementing the Huffman coding in Python.

## Running it

### From the command line

```python
python3 -m huffman -t this is an example of a huffman tree
```

Switches are
* `-t` : display the Huffman tree
* `-c` : display the generated code
* `-e` : encode and decode the given text, print it

## Using it

```python
from huffman import coding, decode, encode, tree, encode_as_bytes, decode_from_bytes


text = "this is an example of a huffman tree"
out = tree.from_string(text)

print(out)
"""
Tree<36, None>(
    Tree<16, 0>(
        Tree<8, 0>(
            <0>('a', 4),
            <1>('e', 4)
        ),
        Tree<8, 1>(
            Tree<4, 0>(
                <0>('t', 2),
                <1>('h', 2)
            ),
            Tree<4, 1>(
                <0>('i', 2),
                <1>('s', 2)
            )
        )
    ),
    Tree<20, 1>(
        Tree<8, 0>(
            Tree<4, 0>(
                <0>('n', 2),
                <1>('m', 2)
            ),
            Tree<4, 1>(
                Tree<2, 0>(
                    <0>('x', 1),
                    <1>('p', 1) 
                ),
                Tree<2, 1>(
                    <0>('l', 1),
                    <1>('o', 1) 
                )
            )
        ),
        Tree<12, 1>(
            Tree<5, 0>(
                Tree<2, 0>(
                    <0>('u', 1),
                    <1>('r', 1) 
                ),
                <1>('f', 3)
            ),
            <1>(' ', 7)
        )
    )
)
"""
print(f"depth: {out.depth}")  # depth 6

print(coding.generate(out))
# {'a': '000', 'e': '001', 't': '0100', 'h': '0101', 'i': '0110', 's': '0111', 'n': '1000',
# 'm': '1001', 'x': '10100', 'p': '10101', 'l': '10110', 'o': '10111', 'u': '11000',
# 'r': '11001', 'f': '1101', ' ': '111'}

print(f"Base text: '{text}', number of bits needed: {len(text) * 8}")
# Base text: 'this is an example of a huffman tree', number of bits needed: 288

e = encode(text, out)
print(f"Encoded text: '{e}', numbers of bits needed: {len(e)}")
# Encoded text: '010001010110011111101100111111000100011100110100000100110101101100011111011111011110001110101110001101110110010001000111010011001001001', numbers of bits needed: 135

d = decode(e, out)
print(f"Decoded text: '{d}'")
# Decoded text: 'this is an example of a huffman tree'

eb = encode_as_bytes(text, out)
print(eb)
# b'"Y}Ob\x1ch\x13-Go^\x1d8nd#S\x12\x02\x01'

db = decode_from_bytes(eb, out)
print(db)
# this is an example of a huffman tree
```