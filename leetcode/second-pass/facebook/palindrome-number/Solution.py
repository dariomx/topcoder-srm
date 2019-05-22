from math import log


class Solution:
    def isPalindrome(self, x):
        base = 10
        if x < 0:
            return False
        if x == 0:
            return True
        n = int(log(x) / log(base))
        pow10 = base ** n
        for _ in range((n + 1) // 2):
            right = x % base
            left = x // pow10
            if right != left:
                return False
            x = x % pow10
            x //= base
            pow10 //= base ** 2
        return True



