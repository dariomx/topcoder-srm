class Solution:
    def __init__(self):
        self.encoder = dict()
        for i in xrange(ord('A'), ord('Z') + 1):
            sym = chr(i)
            digit = i - ord('A')
            self.encoder[digit] = sym
        self.base = len(self.encoder)

    def addOne(self, arr):
        rem = 1
        for i in xrange(len(arr)):
            tmp = arr[i] + rem
            arr[i] = tmp % self.base
            rem = tmp / self.base
        if rem > 0:
            arr.append(0)

    # @param A : integer
    # @return a strings
    def convertToTitle(self, n):
        arr = [0]
        for _ in xrange(n):
            self.addOne(arr)
        return ''.join(map(self.encoder.__getitem__, reversed(arr)))

