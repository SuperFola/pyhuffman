#!/usr/bin/env python3

__all__ = [
    'Node',
    'Tree',
    'from_string',
]


def min_weight(nodes):
    """
    Return the minimum weight of a list of nodes / trees
    """
    if len(nodes) < 2:
        return nodes[0].w
    return min(*nodes, key=lambda n: n.w).w


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


class Node:
    def __init__(self, char: str, w: int):
        self.char = char
        self.w = w
        self.depth = 1
        self.bit = None

    def repr(self, i: int = 0):
        return " " * 4 * i + self.__repr__()

    def __repr__(self) -> str:
        return f"<{self.bit}>('{self.char}', {self.w})"


class Tree:
    @staticmethod
    def from_sorted_list(data: list):
        if len(data) == 2:
            return Tree(*data)

        x, y, *data = data
        trees = [Tree(x, y)]
        min_w = min_weight(data)

        while min_w < trees[-1].w and len(data) >= 2:
            x, y, *data = data
            trees.append(Tree(x, y))

            if len(data) < 2:
                break
            min_w = min_weight(data)

        data = sorted(data + trees, key=lambda n: n.w)
        return Tree.from_sorted_list(data)

    def __init__(self, left, right):
        self.left = left
        self.left.bit = '0'

        self.right = right
        self.right.bit = '1'

        self.bit = None

        self._codes = None

    def _bits_to_list(self):
        bits = []
        if self.bit is not None:
            bits.append(self.bit)

        if isinstance(self.left, Tree):
            bits.append(self.left._bits_to_list())
        else:
            bits.append([self.left])

        if isinstance(self.right, Tree):
            bits.append(self.right._bits_to_list())
        else:
            bits.append([self.right])

        return bits

    def generate_prefixes(self):
        """
        Generate the prefixes for each nodes of the tree
        """
        if self._codes is not None:
            return self._codes

        self._codes = self._bits_to_list()
        self._codes[0] = put_prefix(self._codes[0])
        self._codes[1] = put_prefix(self._codes[1])

        return self._codes

    @property
    def w(self):
        return self.left.w + self.right.w

    @property
    def depth(self):
        return 1 + max(self.left.depth, self.right.depth)

    def repr(self, i: int = 0) -> str:
        pad = " " * 4 * i
        out = pad + f"Tree<{self.w}, {self.bit}>(\n"
        out += self.left.repr(i + 1)
        out += ",\n"
        out += self.right.repr(i + 1)
        out += "\n" + pad + ")"
        return out

    def __repr__(self) -> str:
        return self.repr()


def from_string(buffer: str) -> Tree:
    """
    Create a Huffman tree from a given buffer
    """
    occurences = {}
    for e in buffer:
        if e not in occurences:
            occurences[e] = 1
        else:
            occurences[e] += 1

    occurences = sorted(
        list(Node(c, w) for c, w in occurences.items()),
        key=lambda n: n.w
    )

    return Tree.from_sorted_list(occurences)
