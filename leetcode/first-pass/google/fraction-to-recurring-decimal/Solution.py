class Solution:
    def comp_sign(self, num, denom):
        if num != 0 and (num < 0) != (denom < 0):
            sign = "-"
        else:
            sign = ""
        return sign

    def comp_dec(self, r, denom):
        dec = ""
        idx = dict()
        while r > 0:
            if r in idx:
                i = idx[r]
                dec = "%s(%s)" % (dec[:i], dec[i:])
                break
            else:
                idx[r] = len(dec)
                q, r = divmod(r * 10, denom)
                dec += str(q)
        if dec:
            dec = "." + dec
        return dec

    def fractionToDecimal(self, numerator: 'int', denominator: 'int') -> 'str':
        sign = self.comp_sign(numerator, denominator)
        numerator, denominator = abs(numerator), abs(denominator)
        q, r = divmod(numerator, denominator)
        dec = self.comp_dec(r, denominator)
        return sign + str(q) + dec



