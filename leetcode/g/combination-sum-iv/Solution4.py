class Solution(object):
    def combinationSum4(self, nums, t):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []:
            return 0
        coins = nums
        rec = [0] * (max(t, max(nums)) + 1)
        rec[0] = 0
        for c in coins:
            rec[c] = 1
        for k in xrange(1, t + 1):
            rec[k] += sum([rec[k - c] for c in coins if k - c >= 0])
        return rec[t]
