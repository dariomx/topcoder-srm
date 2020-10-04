class Solution:
    def genPalind(self, size, palind):
        if size == 1:
            return palind.extend("0123456789")
        else:
            self.genPalind(size - 2, palind)
            for i in range(len(palind)):
                for d in "0123456789":
                    palind.append(d + palind[i] + d)

    def isPrime(self, x):
        stop = int(ceil(sqrt(x))) + 1
        for y in range(2, stop):
            if x % y == 0:
                return False
        return True

    def primePalindrome(self, N: int) -> int:
        small = [2, 3, 5, 7, 11]
        i = bisect_left(small, N)
        if i < len(small):
            return small[i]
        size = len(str(N))
        if size % 2 == 0:
            size += 1
        else:
            size += 2
        palind = []
        self.genPalind(size, palind)
        palind = list(map(int, palind))
        heapify(palind)
        while palind:
            x = heappop(palind)
            if len(str(x)) % 2 == 1 and x >= N and self.isPrime(x):
                return x
