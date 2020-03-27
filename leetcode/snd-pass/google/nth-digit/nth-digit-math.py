"""
looks like the pattern is this (x is the one reaching n):

x    y
...
8 -> 8
9 -> 9
10 -> 1
11 -> 0
12 -> 1
13 -> 1
...
186 -> 9
187 -> 8
188 -> 9
189 -> 9
190 -> 1
191 -> 0
192 -> 0
193 -> 1
194 -> 0
195 -> 1
...

This is the series for x given a power k:

https://www.wolframalpha.com/input/?i=sum_%7Bi%3D0%7D%5Ek+sum_%7Bj%3D10%5Ei
%7D%5E%7B10%5E%28i%2B1%29-1%7D+%28i%2B1%29

and this is the corresponding series for y, given same k:

10**(k+1) - 1

"""


class Solution:
    def fx(self, k):
        return int(1 / 9 * (9 * (10 ** (k + 1)) * k + (2 ** (k + 4)) * (
                    5 ** (k + 1)) + 1))

    def fy(self, k):
        return 10 ** (k + 1) - 1

    def bootstrap(self, n):
        k = -1
        x = 0
        y = 0
        while True:
            k += 1
            tx = self.fx(k)
            if tx > n:
                break
            else:
                x = tx
                y = self.fy(k)
        return k, x, y

    def findNthDigit(self, n):
        k, x, y = self.bootstrap(n)
        dx = k + 1
        dy = 1
        hmany = 9 * (10 ** k)
        stop = False
        while x < n and not stop:
            for _ in range(1, hmany + 1):
                x += dx
                y += dy
                if x >= n:
                    stop = True
                    break
            dx += 1
            hmany *= 10
        return str(y)[-(1 + (x - n))]

# test
n = 2147483647
soln = Solution()
k, x, y = soln.bootstrap(n)
print((k, x, y, n-x))