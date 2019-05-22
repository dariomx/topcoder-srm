from bisect import bisect_left


class Solution:
    def similarRGB(self, color):
        X = "0123456789abcdef"
        S = [int("0x%s%s" % (d, d), 16) for d in X]
        hex = lambda s: int(s, 16)
        r, g, b = hex(color[1:3]), hex(color[3:5]), hex(color[5:7])

        def closest(x):
            i = bisect_left(S, x)
            if i - 1 >= 0 and abs(x - S[i - 1]) < abs(x - S[i]):
                d = X[i - 1]
            else:
                d = X[i]
            return d + d

        return "#" + "".join(map(closest, (r, g, b)))

