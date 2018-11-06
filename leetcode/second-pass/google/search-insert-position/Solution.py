class Solution:
    def searchInsert(self, nums, target):
        n = len(nums)
        start, end = 0, n - 1
        while True:
            mid = (start + end) // 2
            x = nums[mid]
            if target == x:
                return mid
            elif target < x:
                end = mid - 1
                if start > end:
                    return start
            else:
                start = mid + 1
                if start > end:
                    return end + 1
