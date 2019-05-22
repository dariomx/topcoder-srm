from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums):
        left = dict()
        right = dict()
        cnt = defaultdict(lambda: 0)
        max_cnt = 0
        for i in range(len(nums)):
            x = nums[i]
            if x not in left:
                left[x] = i
            right[x] = i
            cnt[x] += 1
            max_cnt = max(max_cnt, cnt[x])
        min_len = len(nums)
        for x in nums:
            if cnt[x] == max_cnt:
                min_len = min(min_len, right[x] - left[x] + 1)
        return min_len