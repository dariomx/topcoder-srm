# not mine, python3 adaptation of this awesome soln:
# https://leetcode.com/problems/binary-tree-coloring-game/discuss/367682
# /Simple-Clean-Java-Solution
#
# i missed the fact that once u choose one path (left, right or parent),
# the rest of that
# section is yours

class Solution:
    def count(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.count(node.left) + self.count(node.right)

    def search(self, node, x):
        if node is None:
            return None
        elif node.val == x:
            return node
        else:
            left = self.search(node.left, x)
            if left:
                return left
            else:
                return self.search(node.right, x)

    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        node = self.search(root, x)
        l = self.count(node.left)
        r = self.count(node.right)
        p = n - (l + r + 1)
        return p > (l + r) or l > (p + r) or r > (p + l)
