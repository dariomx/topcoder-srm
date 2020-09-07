class Solution:
    def path2num(self, node, depth, prev):
        num = 0
        pow2 = 1
        while node:
            num += pow2 * node.val
            node = prev[node]
            pow2 <<= 1
        return num

    def sumRootToLeaf(self, root: TreeNode) -> int:
        ans = 0
        prev = dict()
        prev[root] = None
        stack = [(root, None, 0)]
        while stack:
            node, parent, depth = stack.pop()
            prev[node] = parent
            if not node.left and not node.right:
                ans += self.path2num(node, depth, prev)
            for child in (node.left, node.right):
                if child:
                    stack.append((child, node, depth + 1))
        return ans