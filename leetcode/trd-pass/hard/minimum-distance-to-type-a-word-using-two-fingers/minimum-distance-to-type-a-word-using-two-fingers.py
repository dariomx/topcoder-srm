class Solution:
    def minimumDistance(self, word: str) -> int:
        keyb = ['ABCDEF', 'GHIJKL', 'MNOPQR', 'STUVWX', 'YZ']
        pos = {}
        for i in range(len(keyb)):
            for j in range(len(keyb[i])):
                pos[keyb[i][j]] = (i, j)

        def dist(a, b):
            x1, y1 = pos[a]
            x2, y2 = pos[b]
            return abs(x1 - x2) + abs(y1 - y2)

        n = len(word)

        @cache
        def rec(i, f1, f2):
            if i == n:
                return 0
            else:
                return min(rec(i + 1, word[i], f2) + dist(f1, word[i]),
                           rec(i + 1, f1, word[i]) + dist(f2, word[i]))

        ans = inf
        for i in range(n - 1):
            for j in range(i + 1, n):
                ans = min(ans, rec(0, word[i], word[j]))
        return ans
