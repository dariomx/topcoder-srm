# not mine, got it from editorial soln (missed small size of A)

class Solution:
    def getMasks(self, m):
        masks = defaultdict(list)
        for x in range(m):
            nbits = bin(x).count('1')
            masks[nbits].append(x)
        return masks

    def compress(self, x, y):
        for i in reversed(range(len(y))):
            pfx = y[:(i + 1)]
            if x.endswith(pfx):
                return x + y[(i + 1):]
        return x + y

    def shortestSuperstring(self, A: List[str]) -> str:
        n = len(A)
        m = 1 << n
        sizeMasks = self.getMasks(m)
        dp = [[None] * n for _ in range(m)]
        for i in range(n):
            dp[1 << i][i] = A[i]
        for nbits in range(2, n + 1):
            for i in range(n):
                for mask in sizeMasks[nbits - 1]:
                    if (mask & (1 << i)) >> i == 1:
                        continue
                    bestComp = None
                    for j, bit in enumerate(format(mask, '0%db' % n)[::-1]):
                        if bit == '0':
                            continue
                        comp = self.compress(dp[mask][j], A[i])
                        if bestComp is None or len(comp) < len(bestComp):
                            bestComp = comp
                    dp[mask | (1 << i)][i] = bestComp
        return min(dp[m - 1], key=len)


