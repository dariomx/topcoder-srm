"""
looks like the pattern is this (x is the one reaching n, y is the
vertical number holding the associated digits for a range of (k+1) x's):

x    y
...
8 -> 8
9 -> 9      k=0 ends
10 -> 1     k=1 starts
11 -> 0
12 -> 1
13 -> 1
...
186 -> 9
187 -> 8
188 -> 9
189 -> 9    k=1 ends
190 -> 1    k=2 starts
191 -> 0
192 -> 0
193 -> 1
194 -> 0
195 -> 1
...

This is the series for x given a power k:

https://www.wolframalpha.com/input/?i=sum_%7Bi%3D0%7D%5Ek+sum_%7Bj%3D10%5Ei%7D%5E%7B10%5E%28i%2B1%29-1%7D+%28i%2B1%29

and this is the corresponding series for y, given same k:

10**(k+1) - 1

once located the k, we just need to solve this eq to give step
forward (solve for i, in integer floor approx):

x + i*k = n

"""

class Solution:
    def fx(self, k):
        return int(1/9 * (9*(10**(k+1))*k + (2**(k+4))*(5**(k+1)) + 1))

    def fy(self, k):
        return 10**(k+1) - 1

    def bootstrap(self, n):
        k, x, y = -1, 0, 0
        while True:
            k += 1
            tx = self.fx(k)
            if tx > n:
                break
            else:
                x = tx
                y = self.fy(k)
        return k, x, y

    def forward(self, k, x, y, n):
        dx = k + 1
        dy = 1
        if k > 0:
            i = int((n - x) / dx)
            x += i * dx
            y += i * dy
        return x, dx, y, dy

    def findNthDigit(self, n):
        k, x, y = self.bootstrap(n)
        x, dx, y, dy = self.forward(k, x, y, n)
        while x < n:
            x += dx
            y += dy
        return str(y)[-(1 + (x - n))]