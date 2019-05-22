class Solution(object):
    def findMin(self, nums):
        n = len(nums)
        start, end = 0, n - 1
        while start <= end:
            mid = (start + end) // 2
            if mid + 1 < n and nums[mid] > nums[mid + 1]:
                mid = mid + 1
                break
            elif mid - 1 >= 0 and nums[mid - 1] > nums[mid]:
                break
            elif nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        return nums[mid]
