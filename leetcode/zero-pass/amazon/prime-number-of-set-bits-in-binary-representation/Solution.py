"""
Python3 solution using Sieve of Eratosthenes

First, we determine the maximum number of bits in our numbers (nbits)

Then we use Sieve of Eratosthenes to know what numbers are primes for
a representation of nbits.

Finally we iterate over the range, computing the number of set bits for each
number; then we use such value to lookup if is prime or not (if it is,
we count it).

Space is O(nbits) and time is O(R - L + 1), given that computing the number of
set bits is O(1)

"""

from math import log2, ceil


class Solution:
    def countPrimeSetBits(self, L, R):
        nbits = ceil(log2(10 ** 6))

        def sieve(n):
            is_prime = [True] * (n + 1)
            is_prime[1] = False
            for x in range(2, n + 1):
                k = 2
                while True:
                    y = k * x
                    if y > n:
                        break
                    is_prime[y] = False
                    k += 1
            return is_prime

        def countBits(x):
            cnt = 0
            for i in range(nbits):
                cnt += ((1 << i) & x) >> i
            return cnt

        is_prime = sieve(nbits)
        ans = 0
        for x in range(L, R + 1):
            if is_prime[countBits(x)]:
                ans += 1
        return ans
