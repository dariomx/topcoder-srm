class Solution:
    def countVowelStrings(self, n: int, k: int = 5) -> int:
        dp = [1] * k
        for _ in range(2, n + 1):
            psum = [0] * k
            psum[k - 1] = dp[k - 1]
            for i in reversed(range(k - 1)):
                psum[i] = psum[i + 1] + dp[i]
            dp = psum
        return sum(dp)
