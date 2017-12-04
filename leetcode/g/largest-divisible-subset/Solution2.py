from collections import defaultdict
from fractions import gcd as calc_gcd


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        has_one = False
        gcd = defaultdict(lambda: set())
        for i in xrange(n):
            for j in xrange(i + 1, n):
                x = nums[i]
                y = nums[j]
                if 1 in (x, y):
                    has_one = True
                else:
                    k = calc_gcd(x, y)
                    if k > 1 and k in (x, y):
                        gcd[k].add(x)
                        gcd[k].add(y)
        print(gcd)
        keys = gcd.keys()
        m = len(keys)
        for i in xrange(m):
            for j in xrange(i + 1, m):
                k = calc_gcd(keys[i], keys[j])
                if k > 1:
                    gcd[k] |= gcd[keys[i]]
                    gcd[k] |= gcd[keys[j]]
        if gcd:
            max_k = max(gcd, key=lambda k: len(gcd[k]))
            ret = list(gcd[max_k])
        else:
            ret = [max(nums)]
        if has_one:
            ret.append(1)
        return ret
