class Solution:
    @lru_cache(None)
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        ans = []
        if N == 1:
            ans.append(TreeNode(0))
        elif N >= 3:
            N -= 1
            for k in range(1, N):
                for l in self.allPossibleFBT(k):
                    for r in self.allPossibleFBT(N - k):
                        ans.append(TreeNode(0, l, r))
        return ans
