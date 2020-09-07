class Solution:
    def sortString(self, s: str) -> str:
        k = 26
        n = len(s)
        cnt = [0] * k
        base = ord('a')
        for c in s:
            cnt[ord(c) - base] += 1
        ans = ''
        i = 0
        while i < n:
            for j in range(k):
                if cnt[j] > 0:
                    ans += chr(base + j)
                    cnt[j] -= 1
                    i += 1
            for j in reversed(range(k)):
                if cnt[j] > 0:
                    ans += chr(base + j)
                    cnt[j] -= 1
                    i += 1
        return ans


