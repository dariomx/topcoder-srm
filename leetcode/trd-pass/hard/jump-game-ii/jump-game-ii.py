# RMQ is not mine, but taken from
# https://gist.github.com/m00nlight/1f226777a49cfc40ed8f

from math import inf

class RMQ:
    def __init__(self, n):
        self.sz = 1
        while self.sz <= n:
            self.sz = self.sz << 1
        self.dat = [inf] * (2 * self.sz - 1)

    def __setitem__(self, idx, x):
        idx += self.sz - 1
        self.dat[idx] = x
        while idx > 0:
            idx = (idx - 1) >> 1
            self.dat[idx] = min(self.dat[idx * 2 + 1], self.dat[idx * 2 + 2])

    def __getitem__(self, idx):
        return self.query(idx, idx + 1)

    def query(self, a, b):
        return self.query_help(a, b, 0, 0, self.sz)

    def query_help(self, a, b, k, l, r):
        if r <= a or b <= l:
            return inf
        elif a <= l and r <= b:
            return self.dat[k]
        else:
            return min(self.query_help(a, b, 2 * k + 1, l, (l + r)>>1),
                       self.query_help(a, b, 2 * k + 2, (l + r) >> 1, r))

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = RMQ(n)
        dp[n-1] = 0
        for i in reversed(range(n-1)):
            start, end = i + 1, i + nums[i]
            dp[i] = 1 + dp.query(start, end+1)
        return dp[0]
