class Solution:
    @cache
    def fact(self, n):
        if n <= 1:
            return 1
        else:
            return n * self.fact(n-1)

    def getPermK(self, xs: List[int], k: int) -> str:
        n = len(xs)
        if n == 1:
            return str(xs[0])
        elif k == 1:
            return ''.join(map(str, xs))
        else:
            fn_1 = self.fact(n-1)
            q, r = divmod(k, fn_1)
            if q == 0:
                q = 1
            elif r > 0:
                q += 1
            elif r == 0:
                r = fn_1
            pfx = xs[q-1]
            xs = [x for x in xs if x != pfx]
            return str(pfx) + self.getPermK(xs, r)

    def getPermutation(self, n: int, k: int) -> str:
        return self.getPermK(list(range(1, n+1)), k)
