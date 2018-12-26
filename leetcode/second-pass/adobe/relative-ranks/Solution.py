class Solution:
    def findRelativeRanks(self, nums):
        n = len(nums)
        rank = sorted(range(n), reverse=True, key=lambda i: nums[i])
        for i in range(n):
            if i == 0:
                lab = "Gold Medal"
            elif i == 1:
                lab = "Silver Medal"
            elif i == 2:
                lab = "Bronze Medal"
            else:
                lab = str(i+1)
            nums[rank[i]] = lab
        return nums