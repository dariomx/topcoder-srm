class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        wrong = None
        n = len(nums)
        for i in xrange(n - 1):
            if nums[i] > nums[i + 1]:
                if wrong:
                    return False
                else:
                    wrong = (i, i + 1)
        if not wrong:
            return True
        i, j = wrong
        if i == 0 or j == (n - 1):
            return True
        elif nums[i - 1] == nums[j + 1]:
            return (nums[i - 1] == nums[i] or nums[j] == nums[j + 1])
        else:
            return nums[i] <= nums[j + 1]


