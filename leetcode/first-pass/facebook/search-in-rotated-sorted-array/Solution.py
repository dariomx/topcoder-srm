class Solution:
    def findRotIndex(self, nums):
        n = len(nums)
        start, end = 0, n
        while start < end:
            mid = (start + end) // 2
            if mid - 1 >= 0 and nums[mid - 1] > nums[mid]:
                return mid
            elif mid + 1 < n and nums[mid] > nums[mid + 1]:
                return mid + 1
            elif nums[start] > nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return 0

    def binSearch(self, nums, start, end, target):
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def search(self, nums, target):
        n = len(nums)
        if n == 0:
            return -1
        i = self.findRotIndex(nums)
        if i > 0 and nums[0] <= target <= nums[i - 1]:
            return self.binSearch(nums, 0, i - 1, target)
        elif nums[i] <= target <= nums[n - 1]:
            return self.binSearch(nums, i, n - 1, target)
        else:
            return -1



