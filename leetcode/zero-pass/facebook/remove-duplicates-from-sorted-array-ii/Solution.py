class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        k = 2
        j = 0
        def write(i):
            nonlocal j
            nums[j] = nums[i]
            j += 1
        write(0)
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                cnt += 1
                if cnt <= k:
                    write(i)
            else:
                cnt = 1
                write(i)
        return j