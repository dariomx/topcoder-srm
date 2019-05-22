class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.cnt = 0
        n = len(nums)

        def count(sumc):
            print(sumc)
            if sumc == target:
                self.cnt += 1
            elif sumc < target:
                for i in xrange(n):
                    sumc += nums[i]
                    count(sumc)
                    sumc -= nums[i]
                    count(sumc)

        count(0)
        return self.cnt
