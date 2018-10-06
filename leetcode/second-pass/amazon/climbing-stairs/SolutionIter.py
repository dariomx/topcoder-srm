class Solution:
    def climbStairs(self, n):
        if n <= 1:
            return 1
        f1 = 1
        f2 = 1
        for _ in range(2, n + 1):
            tmp = f2
            f2 = f1 + f2
            f1 = tmp
        return f2

