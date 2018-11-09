class Solution:
    def isHappy(self, n):
        sq = lambda m: sum(x**2 for x in map(int, str(m)))
        slow = n
        fast = sq(n)
        while slow != fast:
            slow = sq(slow)
            fast = sq(sq(fast))
        return slow == 1