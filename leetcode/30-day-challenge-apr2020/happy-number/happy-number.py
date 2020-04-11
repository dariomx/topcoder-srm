class Solution:
    def isHappy(self, n):
        prev = set()
        while True:
            n = sum(((ord(d) - 48) ** 2 for d in str(n)))
            if n in prev:
                break
            else:
                prev.add(n)
        return n == 1
