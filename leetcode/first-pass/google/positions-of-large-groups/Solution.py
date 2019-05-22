class Solution:
    def largeGroupPositions(self, S):
        n = len(S)
        start = 0
        prev = None
        ans = []
        for end in range(n):
            if prev and S[end] != prev:
                if end - start >= 3:
                    ans.append((start, end - 1))
                start = end
            prev = S[end]
        if n - start >= 3:
            ans.append((start, end))
        return ans

