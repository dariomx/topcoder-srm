# simplified my original iteration with idea from here
# https://leetcode.com/problems/remove-9/discuss/106553/Simplest-solution
# -ever%3A-2-lines-in-C%2B%2B-(recursive)

class Solution:
    def newInteger(self, n: int) -> int:
        if n < 9:
            return n
        else:
            return 10 * self.newInteger(n // 9) + (n % 9)
