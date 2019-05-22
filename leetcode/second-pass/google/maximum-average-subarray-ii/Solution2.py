class Solution(object):
    def find_maxavg_k(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sumk = 0
        n = len(nums)
        min_nk = min(n, k)
        for i in xrange(min_nk):
            sumk += nums[i]
        mavg = sumk / float(min_nk)
        mavg_idx = (0, min_nk - 1)
        for i in xrange(k, n):
            sumk += nums[i]
            if i >= k:
                sumk -= nums[i - k]
            avg = sumk / float(k)
            if avg > mavg:
                mavg = max(mavg, avg)
                mavg_idx = (max(0, i - k + 1), i)
        return mavg, mavg_idx, sumk

    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        mavg, (i, j), sums = self.find_maxavg_k(nums, k)
        while i > 0 or j < n - 1:
            k += 1
            if i > 0 and j < n - 1:
                avg_left = (sums + nums[i - 1]) / float(k)
                avg_right = (sums + nums[j + 1]) / float(k)
                if avg_left > avg_right:
                    sums += nums[i - 1]
                    i -= 1
                else:
                    sums += nums[j + 1]
                    j += 1
            elif i > 0:
                sums += nums[i - 1]
                i -= 1
            elif j < n - 1:
                sums += nums[j + 1]
                j += 1
            else:
                break
            mavg = max(mavg, sums / float(k))
        return mavg
