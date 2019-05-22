class Solution:
    def addBinary(self, a, b):
        if len(a) < len(b):
            a, b = b, a
        base = 2
        n = len(a)
        m = len(b)
        i = n - 1
        j = m - 1
        rem = 0
        ans = ""
        while i >= 0 and j >= 0:
            tmp = rem + int(a[i]) + int(b[j])
            ans = str(tmp % base) + ans
            rem = tmp // base
            i -= 1
            j -= 1
        if n > m:
            for k in range(i, -1, -1):
                tmp = rem + int(a[k])
                ans = str(tmp % base) + ans
                rem = tmp // base
        if rem > 0:
            ans = str(rem) + ans
        return ans
