class Solution:
    def isPred(self, w1, w2):
        if len(w1) + 1 != len(w2):
            return False
        i = 0
        diff = 0
        for j in range(len(w2)):
            if i < len(w1) and w1[i] == w2[j]:
                i += 1
            else:
                if diff > 0:
                    return False
                diff += 1
        return True

    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=lambda s: len(s))
        n = len(words)
        dp = [1] * n
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if self.isPred(words[i], words[j]):
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
