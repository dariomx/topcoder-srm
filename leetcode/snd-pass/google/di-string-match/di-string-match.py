class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        n = len(S)
        x, y = 0, n
        perm = [None] * (n+1)
        for i in range(n):
            if S[i] == 'I':
                perm[i] = x
                x += 1
            else:
                perm[i] = y
                y -= 1
        perm[n] = y
        return perm