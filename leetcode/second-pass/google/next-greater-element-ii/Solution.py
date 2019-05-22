class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        n = len(nums)
        ans = [-1] * n
        for i in xrange(n):
            for j in xrange(i + 1, i + n):
                if nums[j % n] > nums[i]:
                    ans[i] = nums[j % n]
                    break
        return ans
