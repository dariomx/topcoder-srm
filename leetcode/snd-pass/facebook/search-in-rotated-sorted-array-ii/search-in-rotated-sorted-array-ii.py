from bisect import bisect_left


class Solution:
    def find_pivot(self, nums):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if mid - 1 >= 0 and nums[mid - 1] > nums[mid]:
                return mid
            if nums[start] > nums[mid]:
                if end == mid:
                    end = mid - 1
                else:
                    end = mid
            else:
                if start == mid:
                    start = mid + 1
                else:
                    start = mid
        return 0

    def bin_search(self, nums, x, start, end):
        if start <= end and nums[start] <= x <= nums[end]:
            i = bisect_left(nums, x, start, end + 1)
            if i <= end and nums[i] == x:
                return True
        return False

    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if nums == []:
            return False
        pivot = self.find_pivot(nums)
        if pivot == 0:
            return target in nums
        return self.bin_search(nums, target, 0, pivot - 1) or \
               self.bin_search(nums, target, pivot, n - 1)