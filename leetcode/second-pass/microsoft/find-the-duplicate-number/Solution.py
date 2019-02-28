class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        cand = n * (n + 1) // 2 - sum(nums)
        cnt = 0
        for i in range(n + 1):
            if nums[i] == cand:
                cnt += 1
        if cnt > 1:
            return cand
        else:
            for i in range(n + 1):
                for j in range(i):
                    if nums[i] == nums[j]:
                        return nums[i]
