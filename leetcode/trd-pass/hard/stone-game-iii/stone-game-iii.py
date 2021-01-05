class Solution:
    def stoneGameIII(self, S: List[int]) -> str:
        n = len(S)
        S += [0] * 3
        dp = [[0, 0] for _ in range(n + 3)]
        psum = [0] * (n + 3)
        for i in reversed(range(n)):
            psum[i] = S[i] + psum[i + 1]
            for j in range(2):
                dp[i][j] = max(S[i] + psum[i + 1] - dp[i + 1][1 - j],
                               S[i] + S[i + 1] + psum[i + 2] - dp[i + 2][1 - j],
                               S[i] + S[i + 1] + S[i + 2] + psum[i + 3] -
                               dp[i + 3][1 - j])
        a = dp[0][0]
        b = sum(S) - a
        if a > b:
            return 'Alice'
        elif b > a:
            return 'Bob'
        else:
            return 'Tie'
