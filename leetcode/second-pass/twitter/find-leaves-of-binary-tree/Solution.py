from collections import deque


class Solution:
    def setParent(self, node, parent, leaves):
        if not node:
            return
        if node.left:
            parent[node.left] = node
            self.setParent(node.left, parent, leaves)
        if node.right:
            parent[node.right] = node
            self.setParent(node.right, parent, leaves)
        if not node.left and not node.right:
            leaves.append(node)

    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        parent = dict()
        leaves = deque()
        self.setParent(root, parent, leaves)
        ans = []
        while leaves:
            ans.append([n.val for n in leaves])
            new_leaves = deque()
            while leaves:
                node = leaves.popleft()
                par = parent.get(node, None)
                if not par:
                    continue
                if par.left == node:
                    par.left = None
                if par.right == node:
                    par.right = None
                if not par.left and not par.right:
                    new_leaves.append(par)
            leaves, new_leaves = new_leaves, leaves
        return ans

