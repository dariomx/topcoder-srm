from collections import defaultdict


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        nums.sort()
        has_one = False
        gcd = defaultdict(lambda: set())
        last = dict()
        for i in xrange(n):
            for j in xrange(i + 1, n):
                x = nums[i]
                y = nums[j]
                if 1 in (x, y):
                    has_one = True
                else:
                    if x % y == 0 or y % x == 0:
                        k = min(x, y)
                        gcd[k].add(x)
                        gcd[k].add(y)
                        last[k] = max(x, y)
        print(gcd)
        keys = gcd.keys()
        m = len(keys)
        for i in xrange(m):
            for j in xrange(i + 1, m):
                x = keys[i]
                y = keys[j]
                if x % y == 0 or y % x == 0:
                    k = min(x, y)
                    gcd[k] |= gcd[x]
                    gcd[k] |= gcd[y]
        if gcd:
            max_k = max(gcd, key=lambda k: len(gcd[k]))
            ret = list(gcd[max_k])
        else:
            ret = [max(nums)]
        if has_one:
            ret.append(1)
        return ret
