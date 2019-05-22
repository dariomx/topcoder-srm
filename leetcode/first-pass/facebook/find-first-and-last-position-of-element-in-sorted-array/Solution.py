class Solution:
    def binSearchLeft(self, nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                if mid == 0 or nums[mid - 1] < target:
                    return mid
                else:
                    end = mid - 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def binSearchRight(self, nums, target):
        n = len(nums)
        start, end = 0, n - 1
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                if mid == n - 1 or nums[mid + 1] > target:
                    return mid
                else:
                    start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def searchRange(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        return [self.binSearchLeft(nums, target),
                self.binSearchRight(nums, target)]

