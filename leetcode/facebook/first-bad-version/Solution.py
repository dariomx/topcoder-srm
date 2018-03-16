class Solution(object):
    def firstBadVersion(self, n):
        start, end = 1, n
        while start < end:
            mid = (start + end)//2
            if not isBadVersion(mid) and isBadVersion(end):
                start = mid+1
            else:
                end = mid
        return start
