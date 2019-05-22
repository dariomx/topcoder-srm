class Solution:
    def isPerfectSquare(self, num):
        start = 1
        end = num
        while start <= end:
            mid = (start + end) // 2
            sq = mid * mid
            if sq == num:
                return True
            elif sq < num:
                start = mid + 1
            else:
                end = mid - 1
        return False

