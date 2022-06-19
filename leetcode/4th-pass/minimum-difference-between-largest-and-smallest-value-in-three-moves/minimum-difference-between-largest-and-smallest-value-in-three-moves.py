class Solution:        
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0
        else:
            nums.sort()
        
        ans = inf
        for i in range(4):
            j = 3 - i
            ans = min(ans, nums[-1-j] - nums[i])
        return ans
            
