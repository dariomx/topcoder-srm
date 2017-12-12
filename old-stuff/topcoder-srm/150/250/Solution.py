class InterestingDigits:
    def isInteresting(self, digit, x, base):
        decX = 0
        powB = 1
        while x >= base:
            decX += powB * (x % base)
            x = x / base
        decX += powB * x
        return decX % digit == 0

    def digits(self, base):
        ret = []
        maxX = base*base*(base-1) + base*(base-1) + (base-1)
        for digit in xrange(2, base):
            x = 2 * digit
            fail = False
            while x <= maxX and not fail:
                if not self.isInteresting(digit, x, base):
                    fail = True
                else:
                    x += digit
            if not fail:
                ret.append(digit)
        return ret

print(InterestingDigits().digits(30))