class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.space = end - start
        self.left = None
        self.right = None


def build_tree(node):
    if node.end - node.start <= 1:
        return
    split = (node.start + node.end) / 2
    node.left = Node(node.start, split)
    node.right = Node(split, node.end)
    build_tree(node.left)
    build_tree(node.right)


def find_pos(node, infront):
    node.space -= 1
    if node.left is None:
        return node.start
    if node.left.space > infront:
        return find_pos(node.left, infront)
    else:
        return find_pos(node.right, infront - node.left.space)


class Solution:
    def order(self, heights, infronts):
        ret = [0] * len(heights)
        root = Node(0, len(heights))
        build_tree(root)

        for (h, i) in sorted(zip(heights, infronts)):
            pos = find_pos(root, i)
            ret[pos] = h

        return ret


