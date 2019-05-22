class Solution(object):
    def intToRoman(self, num):
        def roman(x, unit, middle, high):
            if x == 4:
                r = unit + middle
            elif x == 9:
                r = unit + high
            else:
                r = unit * (x % 5)
                if x >= 5:
                    r = middle + r
            return r

        sym = ['I', 'V', 'X', 'L', 'C', 'D', 'M', None, None]
        i = 0
        ans = ''
        while num > 0:
            ans = roman(num % 10, sym[i], sym[i + 1], sym[i + 2]) + ans
            num //= 10
            i += 2
        return ans

