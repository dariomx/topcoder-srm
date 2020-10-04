class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = defaultdict(lambda: 0)
        S = sum(nums)
        for x in nums:
            q, r = divmod(S - x, 3)
            if r == 0 and 3*q + x == S:
                cnt[x] += 1
        for x, k in cnt.items():
            if k == 1:
                return x