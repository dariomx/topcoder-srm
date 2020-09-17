class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        i = bisect_left(nums, target)
        if i == 0 and nums[i] != target:
            return False
        j = bisect_right(nums, target)
        if j == n:
            if nums[-1] != target:
                return False
            else:
                j -= 1
        return j - i + 1 > n // 2