from collections import Counter


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        k = 101
        cnt = [0] * k
        for x in nums:
            cnt[x] += 1
        lt = [0] * k
        size = len(nums)
        for x in reversed(range(k)):
            if cnt[x] == 0:
                continue
            size -= cnt[x]
            lt[x] = size
        return [lt[x] for x in nums]
