"""
Sort of DP solution here:

P[i] = # solutions ending at i-th position with Present
A[i] = # "          "          "              " Absence
L[i] = # "          "          "              " Late

P[i] = sum of previous row A[i-1] + L[i-1] + P[i-1], as the Presence can be combined without restrictions to any smaller solution.

A[i] happens to be tribonacci (https://oeis.org/A000073), cause it is a solution to the sub-problem where Absences do not play.

L[i] happens to be a weird thing: P[i] minus https://oeis.org/A073778. That series we substract is kinda tribonacci but with some weights (see cited page at formulas section, for 2014 Weiner result). The semantics of A073778 is "Number of binary sequences of length n+1 that have exactly one subsequence 000"; I suspect this relates to the odd interaction between Absences and cases like 'LLL', which A[i] does not generate but which can lead to valid combos 'LLAL' or 'LALL'. One beer for a clearer insight ;-?

Note: there is an unwanted side effect of depending on A073778, and it is its division operation, which we would need to make modulo M. Unlike the addition, division requires a more elaborated adaptation in modular arithmetic. Took this part from

https://www.geeksforgeeks.org/modular-division/

Ok, ok ... forcing our solution to use A073778 rather than simpler formulations, seems to make this unnecessarily expensive due the modular division ... but I could not resist using this strange connection with A073778 ;-?
"""

from math import gcd

class Solution:
    def modInverse(self, b, m):
        g = gcd(b, m)
        if (g != 1):
            raise ValueError('Inverse does not exist')
        else:
            return pow(b, m - 2, m)

    # Function to compute a/b under modulo m
    def modDivide(self, a, b, m):
        a = a % m
        inv = self.modInverse(b, m)
        if(inv == -1):
            raise ValueError('Division not defined')
        else:
            return (inv*a) % m

    def checkRecord(self, n: int) -> int:
        P = [1, 3, 8]
        A = [1, 2, 4]
        S = [0, 0, 1]
        L = [1, 3, 7]
        M = 10**9 + 7
        if n > 2:
            for i in range(3, n):
                P = P[-2], P[-1], (A[-1] + L[-1] + P[-1]) % M
                A = A[-2], A[-1], sum(A) % M
                numS = (i-1)*S[-1] + i*S[-2] + (i+1)*S[-3]
                denS = i - 2
                A073778 = self.modDivide(numS, denS, M)
                S = S[-2], S[-1], A073778
                L = L[-2], L[-1], (P[-1] - S[-1]) % M
        else:
            for _ in range(3-n):
                P.pop()
                A.pop()
                L.pop()
        return (P[-1] + A[-1] + L[-1]) % M
