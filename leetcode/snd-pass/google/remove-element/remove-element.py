from math import inf


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == val:
                nums[i] = inf
                cnt += 1
        nums.sort()
        return n - cnt
