class Solution:
    def convertToBase7(self, num):
        if num == 0:
            return "0"
        base = 7
        ans = ""
        sign = "" if num >= 0 else "-"
        num = abs(num)
        while num > 0:
            q, r = divmod(num, base)
            ans = str(r) + ans
            num = q
        return sign + ans