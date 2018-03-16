from collections import defaultdict
from sys import maxsize as maxint


class Solution:
    def threeSum(self, nums):
        n = len(nums)
        sum2 = defaultdict(lambda: [])
        minn, maxn = maxint, -maxint
        for i in range(n):
            y = nums[i]
            minn = min(minn, y)
            maxn = max(maxn, y)
            for j in range(i + 1, n):
                sum2[y + nums[j]].append((i, j))
        base = maxn - minn + 1

        def calc_key(x, y, z):
            arr = sorted((x, y, z))
            key = 0
            for i in range(2):
                key += (base ** i) * arr[i]
            return key

        triples = []
        used = dict()
        for k in range(n):
            x = nums[k]
            if -x in sum2:
                for i, j in sum2[-x]:
                    if k == i or k == j:
                        continue
                    y, z = nums[i], nums[j]
                    key = calc_key(x, y, z)
                    if key not in used:
                        used[key] = True
                        triples.append((x, y, z))
        return triples

