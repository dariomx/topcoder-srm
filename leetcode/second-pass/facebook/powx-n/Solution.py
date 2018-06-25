class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = abs(n)
        parity = []
        while n > 0:
            parity.append(n % 2)
            n //= 2
        powx = x
        for i in reversed(range(len(parity)-1)):
            powx *= powx
            if parity[i] == 1:
                powx *= x
        return powx
