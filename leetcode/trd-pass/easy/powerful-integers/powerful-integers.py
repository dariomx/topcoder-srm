class Solution:
    def maxIx(self, a, bound):
        if a < 2:
            den = 1
        else:
            den = log(a)
        return int(log(max(1, bound - 1)) / den)

    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        max_i = self.maxIx(x, bound)
        max_j = self.maxIx(y, bound)
        ans = set()
        for i in range(max_i + 1):
            for j in range(max_j + 1):
                p = x ** i + y ** j
                if p <= bound:
                    ans.add(p)
        return list(ans)