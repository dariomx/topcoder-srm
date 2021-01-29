class Solution:
    def newInteger(self, n: int) -> int:
        if n < 9:
            return n
        else:
            for x in range(n, n - 9, -1):
                q, r = divmod(x, 9)
                if r == 0:
                    return 10 * self.newInteger(q) + (n - x)


