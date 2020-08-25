class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        rSum = 0
        for x in nums:
            rSum += x
            ans.append(rSum)
        return ans