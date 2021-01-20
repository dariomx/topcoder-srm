# this is brute force!

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        ans = ''
        cnt = 0
        prev = None
        rec = False
        for c in (s + '$'):
            if c == prev:
                cnt += 1
                if cnt == k:
                    cnt = 0
                    rec = True
            else:
                if prev:
                    ans += prev * cnt
                prev = c
                cnt = 1
        if rec:
            return self.removeDuplicates(ans, k)
        else:
            return ans
