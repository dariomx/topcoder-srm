class Solution:
    def searchInsert(self, nums, target):
        n = len(nums)
        start, end = 0, n-1
        while start <= end:
            mid = (start + end) // 2
            x = nums[mid]
            if target == x:
                return mid
            elif target < x:
                end = mid - 1
            else:
                start = mid + 1
        return end + 1        