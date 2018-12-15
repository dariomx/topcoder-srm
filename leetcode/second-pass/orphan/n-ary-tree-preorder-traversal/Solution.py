class Solution(object):
    def preorder(self, root):
        ans = []

        def rec(node):
            if node:
                ans.append(node.val)
                for child in node.children:
                    rec(child)

        rec(root)
        return ans
