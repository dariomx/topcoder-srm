from collections import defaultdict


class Solution:
    def majorityElement(self, nums):
        cnt = defaultdict(lambda: 0)
        mc = len(nums) // 2
        for x in nums:
            cnt[x] += 1
            if cnt[x] > mc:
                return x
