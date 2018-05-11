class Solution:
    def romanToInt(self, s):
        rom2dec = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        dnum = 0
        prev = None
        for c in s:
            curr = rom2dec[c]
            dnum += curr
            if prev and prev < curr:
                dnum -= 2 * prev
            prev = curr
        return dnum
