class Solution:
    def mySqrt(self, x):
        if x == 0:
            return 0
        sqr = x
        while True:
            next = 1 / 2 * (sqr + x / sqr)
            if int(sqr) == int(next):
                break
            else:
                sqr = next
        return int(sqr)
