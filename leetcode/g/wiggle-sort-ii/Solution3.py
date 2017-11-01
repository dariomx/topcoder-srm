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
        middle_val = nums[middle]
        wiggle = zip(nums[:middle], nums[middle + n % 2:])
        sort_wiggle = False
        for i in xrange(middle - 1):
            if wiggle[i][1] == wiggle[i + 1][0]:
                sort_wiggle = True
                break
        if sort_wiggle:
            wiggle.sort(reverse=True)
        j = 0
        for i in xrange(middle):
            nums[j], nums[j + 1] = wiggle[i]
            j += 2
        if n % 2 == 1:
            nums[n - 1] = middle_val
