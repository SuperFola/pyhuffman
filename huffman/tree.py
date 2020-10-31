#!/usr/bin/env python3

def min_weight(nodes):
    if len(nodes) < 2:
        return nodes[0].w
    return min(*nodes, key=lambda n: n.w).w


class Node:
    def __init__(self, char: str, w: int):
        self.char = char
        self.w = w

    def repr(self, i: int = 0):
        return " " * 4 * i + self.__repr__()

    def __repr__(self) -> str:
        return f"('{self.char}', {self.w})"


class Tree:
    @staticmethod
    def from_list(data: list):
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
        return Tree.from_list(data)

    def __init__(self, left, right):
        self.left = left
        self.right = right

    @property
    def w(self):
        return self.left.w + self.right.w

    def repr(self, i: int = 0) -> str:
        pad = " " * 4 * i
        out = pad + f"Tree<{self.w}>(\n"
        out += self.left.repr(i + 1)
        out += ",\n"
        out += self.right.repr(i + 1)
        out += "\n" + pad + ")"
        return out

    def __repr__(self) -> str:
        return self.repr()