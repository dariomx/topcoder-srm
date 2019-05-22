class Solution:
    def preord(self, root):
        if root:
            yield from self.preord(root.left)
            yield root
            yield from self.preord(root.right)

    def set_values(self, root):
        i = 1
        for node in self.preord(root):
            node.val = i
            i = i + 1

    def clone(self, root):
        if root is None:
            return None
        else:
            ret = TreeNode(root.val)
            ret.left = self.clone(root.left)
            ret.right = self.clone(root.right)
            return ret

    def generateTrees(self, n: int) -> List[TreeNode]:
        def search(total, frontier):
            if total == n:
                self.set_values(root)
                ans.append(self.clone(root))
            else:
                node, pend = frontier.pop()
                for i in range(pend + 1):
                    j = pend - i
                    kids = []
                    k_total = total
                    if i > 0:
                        k_total += 1
                        node.left = TreeNode(None)
                        kids.append((node.left, i - 1))
                    if j > 0:
                        k_total += 1
                        node.right = TreeNode(None)
                        kids.append((node.right, j - 1))
                    search(k_total, frontier + kids)
                    node.left = None
                    node.right = None

        # main
        ans = []
        if n > 0:
            root = TreeNode(None)
            search(1, [(root, n - 1)])
        return ans
