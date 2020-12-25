class Solution:
    def decodeStep(self, enc):
        openBra = enc.find('[')
        if openBra < 0:
            return 1, enc
        else:
            closeBra = enc.find(']')
            cnt = int(enc[:openBra])
            pat = enc[(openBra + 1):closeBra]
            return cnt, pat

    def merge(self, enc1, enc2):
        cnt1, pat1 = self.decodeStep(enc1)
        cnt2, pat2 = self.decodeStep(enc2)
        if pat1 == pat2:
            return '%d[%s]' % (cnt1 + cnt2, pat1)
        elif cnt1 == 1 == cnt2:
            return pat1 + pat2
        else:
            return enc1 + enc2

    def encode(self, s: str) -> str:
        n = len(s)
        dp = [[None] * n for _ in range(n + 1)]
        for i in range(n):
            dp[0][i] = s
            dp[1][i] = s[i]
        for size in range(2, n + 1):
            for i in range(n - size + 1):
                j = i + size - 1
                dp[size][i] = s[i:(j + 1)]
                for k in range(i + 1, j + 1):
                    dp[size][i] = min(dp[size][i],
                                      self.merge(dp[k][i], dp[j - k + 1][k]),
                                      key=len)
        return dp[n][0]

print(Solution().encode("aaaa"))
