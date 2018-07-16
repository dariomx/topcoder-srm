class Solution:
    def romanToInt(self, s):
        val = {'I':1, 'V':5, 'X':10, 'L':50,
               'C':100, 'D':500, 'M':1000}
        n = len(s)
        dec = 0
        last = 0
        for i in range(n-1, -1, -1):
            curr = val[s[i]]
            sign = -1 if curr < last else +1
            dec += sign * curr
            last = curr
        return dec