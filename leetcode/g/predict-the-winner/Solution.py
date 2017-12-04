class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 0:
            return False
        pfx_sum = [0] * n
        pfx_sum[0] = nums[0]
        for i in xrange(1, n):
            pfx_sum[i] += pfx_sum[i - 1] + nums[i]

        def get_sum(start, end):
            return pfx_sum[end] - pfx_sum[start] + nums[start]

        def get_max(start, end):
            if start > end:
                return 0
            elif start == end:
                return nums[start]
            else:
                sub_sum = get_sum(start, end)
                left_max = nums[start] + (sub_sum - get_max(start + 1, end))
                right_max = nums[end] + (sub_sum - get_max(start, end - 1))
                return max(left_max, right_max)

        start_max = get_max(0, n - 1)
        total_sum = get_sum(0, n - 1)
        return start_max >= (total_sum - start_max)
