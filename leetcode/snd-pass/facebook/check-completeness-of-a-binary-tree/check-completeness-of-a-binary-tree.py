class Solution:
    def dfs(self, root, path, depth):
        if root:
            self.max_depth = max(self.max_depth, depth)
            if depth == self.max_depth and \
                    root.left is None and root.right is None:
                if self.leaf == path:
                    self.leaf += 1
                else:
                    raise ValueError()
            else:
                self.non_leaf += 1
                self.dfs(root.left, 2 * path, depth + 1)
                self.dfs(root.right, 2 * path + 1, depth + 1)

    def isCompleteTree(self, root: TreeNode) -> bool:
        self.max_depth = 0
        self.leaf = 0
        self.non_leaf = 0
        try:
            self.dfs(root, 0, 0)
            return self.non_leaf == 2 ** self.max_depth - 1
        except ValueError:
            return False