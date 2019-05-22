class Solution:
    def get_sign(self, x, y):
        if (x >= 0 and y >= 0) or (x < 0 and y < 0):
            return +1
        else:
            return -1

    def divide(self, dividend, divisor):
        sign = self.get_sign(dividend, divisor)

        def rec(x, y, powy, logy):
            if x < y:
                return 0
            else:
                n_powy = powy + powy
                n_logy = logy + logy
                if n_powy > x:
                    return logy + rec(x - powy, y, y, 1)
                else:
                    return rec(x, y, n_powy, n_logy)

        x, y = abs(dividend), abs(divisor)
        ans = sign * rec(x, y, y, 1)
        return max(-2147483648, min(2147483647, ans))
