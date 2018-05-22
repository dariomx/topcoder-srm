class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        wrong = 0
        for i in xrange(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if wrong > 0:
                    return False
                elif (i == 0 or nums[i - 1] <= nums[i + 1]) or \
                        (i + 1 == (len(nums) - 1) or nums[i] <= nums[i + 2]):
                    wrong += 1
        return True
