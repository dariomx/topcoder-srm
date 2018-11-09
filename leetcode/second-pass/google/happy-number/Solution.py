class Solution:
    def isHappy(self, n):
        seen = set()
        while n not in seen and n != 1:
            seen.add(n)
            n = sum(x**2 for x in map(int, str(n)))
        return n == 1