class Solution(object):
    def guessNumber(self, n):
        start, end = 1, n
        while start <= end:
            mid = (start + end) // 2
            cmp = guess(mid)
            if cmp == 0:
                return mid
            elif cmp < 0:
                end = mid - 1
            else:
                start = mid + 1
        return -1