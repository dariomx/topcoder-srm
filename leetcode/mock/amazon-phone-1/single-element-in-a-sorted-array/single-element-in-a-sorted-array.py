class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = 0, n - 1
        while start <= end:
            mid = (start + end) // 2
            if (mid == 0 or nums[mid - 1] < nums[mid]) and \
                    (mid == n - 1 or nums[mid] < nums[mid + 1]):
                return nums[mid]
            elif mid + 1 < n and nums[mid] == nums[mid + 1]:
                if mid % 2 == 0:
                    start = mid + 1
                else:
                    end = mid - 1
            elif mid - 1 >= 0 and nums[mid - 1] == nums[mid]:
                if (mid - 1) % 2 == 0:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                raise ValueError('Invalid state')
        raise ValueError('Could not find it')
