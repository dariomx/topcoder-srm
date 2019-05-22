"""
Python3 solution using Sieve of Eratosthenes, time is O(n)

The big trick here is to avoid the quadratic complexity, and despite
intuition we can do that even with a nested loop (a friend of mine, who is
studying a Msc in Computer Science, reminded me that it does not matter how
many loops you nest; what matters for time complexity is how many times you
process the elements).

What I recall from Sieve of Eratosthenes, is that you checked sequentially
the numbers; for each one you iterate over its multiples and discard them (
if they are multiples, then they are not primes). At the end of this
procedure, you end up with only prime numbers.

Then, our main loop keeps track of what is next number to check. We use an
array for quickly checking whether a number has been discarded, so we do not
process them more than once. A known result tells that we do not need to
check beyond sqrt(n), in the outer loop; so we leverage that.

Note: my original code did not use the sqrt(n) optimization, because I was
stubborn in not doing a final pass to compute the count; in exchange I was
using a counter to keep track of how many elements I processed so far. But
using the sqrt(n) resulted in shorter and faster code.
"""

from math import sqrt


class Solution:
    def countPrimes(self, n):
        if n <= 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False
        sn = int(sqrt(n)) + 1
        for x in range(2, sn):
            if is_prime[x]:
                k = 2
                while True:
                    fx = k * x
                    if fx >= n:
                        break
                    is_prime[fx] = False
                    k += 1
        return sum(is_prime)
