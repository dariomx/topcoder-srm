from math import log

class Solution:
    def __init__(self):
        self.encoder = dict()
        for i in xrange(ord('A'), ord('Z') + 1):
            sym = chr(i)
            digit = i - ord('A')
            self.encoder[digit] = sym
        self.base = len(self.encoder)

    def changeBase(self, num):
        arr = []
        while True:
            arr.append(num % self.base)
            num = num / self.base
            if num == 0:
                break;
        return arr

    def getShift(self, num):
        shift = 0
        if num < self.base:
            n = 1
        else:
            n = int(log(num) / log(self.base)) + 1
            for k in xrange(1, n):
                shift += self.base**k
            if shift > num:
                shift -= self.base**(n-1)
                n -= 1
        return shift, n

    def rightPad(self, arr, n):
        for _ in xrange(n - len(arr)):
            arr.append(0)

    def encode(self, arr):
        return ''.join(map(self.encoder.__getitem__, reversed(arr)))

    # @param A : integer
    # @return a strings
    def convertToTitle(self, num):
        num -= 1
        shift, n = self.getShift(num)
        arr = self.changeBase(num - shift)
        self.rightPad(arr, n)
        return self.encode(arr)

num = 749746
num = 26
num = 27*26
print(Solution().convertToTitle(num))
