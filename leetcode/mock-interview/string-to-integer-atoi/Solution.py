class Solution:
    def myAtoi(self, str):
        i = 0
        n = len(str)
        while i < n and str[i] == ' ':
            i += 1
        sign = 1
        if i < n and str[i] == '-':
            i += 1
            sign = -1
        start = i
        while i < n and 48 <= ord(str[i]) <= 57:
            i += 1
        end = i - 1
        pow10 = 1
        myint = 0
        for i in range(end, start - 1, -1):
            myint += pow10 * (48 - ord(str[i]))
            pow10 *= 10
        myint = sign * myint
        if myint < -2147483648:
            return -2147483648
        elif myint > 2147483647:
            return 2147483647
        else:
            return myint
