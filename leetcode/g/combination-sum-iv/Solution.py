from collections import defaultdict


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        comb = defaultdict(lambda: 0)
        for k in xrange(1, target + 1):
            for x in nums:
                if x == k:
                    comb[k] += 1
        for n in xrange(2, len(nums) + 1):
            for k in xrange(1, target + 1):
                for m in xrange(1, k / 2 + 1):
                    if m != k - m:
                        args = (n, k, m, comb[k], comb[m], comb[k - m],
                                comb[k] + comb[m] * comb[k - m])
                        print("%d,%d,%d: %d + %d * %d = %d" % (args))
                        comb[k] += comb[m] * comb[k - m]
        return comb[target]
