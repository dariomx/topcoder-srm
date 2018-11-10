class Solution:
    def isPerfectSquare(self, num):
        for x in range(1, num+1):
            sq = x*x
            if sq == num:
                return True
            elif sq > num:
                return False