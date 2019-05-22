class Solution:
    def toHex(self, num):
        base = 16
        enc = {10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}
        if num < 0:
            num = (1<<32) + num
        ans = ""
        while num > 0:
            q, r = divmod(num, base)
            ans = (str(r) if r < 10 else enc[r]) + ans
            num = q
        return "0" if len(ans)==0 else ans