
class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            ans = 0
            for c in root.children:
                ans = max(ans, self.maxDepth(c))
            return 1 + ans