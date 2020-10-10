# not mine, saw explanation in phorum

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @lru_cache(None)
        def rec(start, end):
            ret = 0
            for i in range(start, end + 1):
                coins = nums[start - 1] * nums[i] * nums[end + 1] + \
                        rec(start, i - 1) + rec(i + 1, end)
                ret = max(ret, coins)
            return ret

        nums = [1] + nums + [1]
        return rec(1, len(nums) - 2)
