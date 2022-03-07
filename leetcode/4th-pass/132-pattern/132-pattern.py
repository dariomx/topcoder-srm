from sortedcontainers import SortedList

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        lmin = nums[0]
        rsort = SortedList(nums[1:])
        for i, x in enumerate(nums[1:]):
            lmin = min(lmin, x)
            rsort.remove(x)
            if lmin >= x:
                continue
            between = rsort.irange(lmin, x, inclusive=(False, False))
            if any(True for _ in between):
                return True
        return False