# we explore the usage of delete-only distance (variation of edit-distance von
# Levenshtein)

from math import inf

# min # of deletions to transform s into t
def del_dist(s, t):
    m, n = len(s), len(t)
    assert m >= n
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        dp[i][0] = i
    for j in range(1, n+1):
        dp[0][j] = inf
    for j in range(1, n+1):
        for i in range(1, m+1):
            if s[i-1] == t[j-1]:
                subsCost = 0
            else:
                subsCost = inf
            dp[i][j] = min(dp[i-1][j] + 1, dp[i-1][j-1] + subsCost)
    return dp[m][n]

# main
S = "abcdebdde"
T = "bde"
print(del_dist(S, T))
