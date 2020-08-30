from math import factorial as fact, sqrt


class Solution:
    def isPrime(self, x):
        for d in range(2, int(sqrt(x)) + 1):
            if x % d == 0:
                return False
        return True

    def numPrimeArrangements(self, n: int) -> int:
        m = sum(map(self.isPrime, range(2, n + 1)))
        return (fact(m) * fact(n - m)) % (10 ** 9 + 7)