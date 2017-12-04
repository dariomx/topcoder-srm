class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.cnt = 0
        n = len(nums)

        def count(i, sumc):
            print(sumc)
            if sumc == target:
                self.cnt += 1
            elif i < n:
                sumc += nums[i]
                count(i + 1, sumc)
                sumc -= nums[i]
                count(i + 1, sumc)

        count(0, 0)
        return self.cnt
