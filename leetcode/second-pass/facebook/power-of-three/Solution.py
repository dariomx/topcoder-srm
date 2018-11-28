class Solution:
    def isPowerOfThree(self, n):
        k = 3
        ones_basek = 0
        while n > 0:
            ones_basek += n % k
            n //= k
            if ones_basek > 1:
                return False
        return ones_basek == 1
