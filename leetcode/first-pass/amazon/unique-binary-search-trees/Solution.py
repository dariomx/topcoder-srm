class Solution:
    def __init__(self):
        self.cache = {}

    def numTrees(self, n: int) -> int:
        if n <= 0:
            return 1
        elif n in self.cache:
            return self.cache[n]
        else:
            ans = 0
            for i in range(1, n + 1):
                ans += self.numTrees(i - 1) * self.numTrees(n - i)
            self.cache[n] = ans
            return ans
