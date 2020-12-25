class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def rec(i, j, dist):
            nonlocal ans
            if i == n and j == m:
                ans = min(ans, dist)
            elif i < n and j == m:
                ans = min(ans, dist + (n - i))  # rest are deletes
            elif i == n and j < m:
                ans = min(ans, dist + (m - j))  # rest are inserts
            elif dist <= ans:
                if word1[i] == word2[j]:
                    rec(i + 1, j + 1, dist)  # equal
                else:
                    rec(i + 1, j + 1, dist + 1)  # replace
                rec(i + 1, j, dist + 1)  # delete
                rec(i, j + 1, dist + 1)  # insert

        n, m = len(word1), len(word2)
        ans = inf
        rec(0, 0, 0)
        return ans
