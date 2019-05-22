# adapted from https://en.wikipedia.org/wiki/Knapsack_problem#0
# /1_knapsack_problem

class Solution:
    def findMaxForm(self, strs, m, n):
        def weight(s):
            zeros, ones = 0, 0
            for i in xrange(len(s)):
                if s[i] == '0':
                    zeros += 1
                else:
                    ones += 1
            return zeros, ones

        k = len(strs)
        rec = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(k + 1)]
        for i in xrange(m + 1):
            for j in xrange(n + 1):
                rec[0][i][j] = 0
        for l in xrange(1, k + 1):
            w = weight(strs[l - 1])
            for i in xrange(m + 1):
                for j in xrange(n + 1):
                    if w[0] > i or w[1] > j:
                        rec[l][i][j] = rec[l - 1][i][j]
                    else:
                        rec[l][i][j] = max(rec[l - 1][i][j],
                                           rec[l - 1][i - w[0]][j - w[1]] + 1)
        return rec[k][m][n]
