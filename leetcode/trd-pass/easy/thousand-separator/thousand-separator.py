class Solution:
    def thousandSeparator(self, n: int) -> str:
        ans = ''
        cnt = 0
        s = str(n)
        for i in range(len(s)-1, -1, -1):
            cnt += 1
            ans += s[i]
            if cnt % 3 == 0 and i > 0:
                ans += '.'
        return ans[::-1]