class Solution:
    def __init__(self):
        self.cache = {}

    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N in self.cache:
            return self.cache[N]
        ans = []
        if N == 1:
            ans.append(TreeNode(0))
        elif N >= 3:
            self.cache[N] = ans
            N -= 1
            for k in range(1, N):
                left = self.allPossibleFBT(k)
                right = self.allPossibleFBT(N - k)
                for l in left:
                    for r in right:
                        ans.append(TreeNode(0, l, r))
        return ans
