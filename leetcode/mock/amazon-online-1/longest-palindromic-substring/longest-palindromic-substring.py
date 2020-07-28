class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        cand1 = [(i, i) for i in range(n)]
        cand2 = [(i, i+1) for i in range(n-1) if s[i] == s[i+1]]
        fst = cand2[0] if cand2 else (cand1[0] if cand1 else None)
        if fst:
            i, j = fst
            ans = s[i:j+1]
        else:
            ans = ''
        cand = cand1 + cand2
        while cand:
            i, j = cand.pop()
            ni, nj = i-1, j+1
            if ni >= 0 and nj < n and s[ni] == s[nj]:
                cand.append((ni, nj))
                if nj - ni + 1 > len(ans):
                    ans = s[ni:nj+1]
        return ans