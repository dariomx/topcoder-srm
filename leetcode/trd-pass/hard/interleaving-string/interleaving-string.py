class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def rec(k, i, j, n, m, turn):
            if k == len(s3):
                return i == len(s1) and j == len(s2) and abs(m - n) <= 1
            if i < len(s1) and s3[k] == s1[i]:
                if rec(k + 1, i + 1, j, n + int(turn != 1), m, 1):
                    return True
            if j < len(s2) and s3[k] == s2[j]:
                if rec(k + 1, i, j + 1, n, m + int(turn != 2), 2):
                    return True
            return False

        if len(s1) + len(s2) != len(s3):
            return False
        else:
            return rec(0, 0, 0, 0, 0, None)

