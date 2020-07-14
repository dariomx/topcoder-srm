class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        prev = nums[0]
        for x in nums[1:]:
            n_miss = x - prev - 1
            if n_miss >= k:
                break
            else:
                k -= n_miss
                prev = x
        return prev + k