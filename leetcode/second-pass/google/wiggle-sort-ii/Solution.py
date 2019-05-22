class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        middle = n / 2
        if n % 2 == 1:
            nums[middle], nums[-1] = nums[-1], nums[middle]
        right = middle + 1
        for left in xrange(1, middle, 2):
            nums[left], nums[right] = nums[right], nums[left]
            right += 2
            # if nums[middle - 1] == nums[middle]:
