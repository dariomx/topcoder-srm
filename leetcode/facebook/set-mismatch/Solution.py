class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        found = [False] * (n+1)
        dup = None
        sum = 0
        for x in nums:
            if found[x]:
                dup = x
            else:
                found[x] = True
                sum += x
        return [dup, n*(n+1)//2 - sum]