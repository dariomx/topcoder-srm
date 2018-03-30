from collections import defaultdict


class Solution:
    def fourSum(self, nums, target):
        sum2 = defaultdict(lambda: [])
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                sum2[nums[i] + nums[j]].append((i, j))
        quads = set()
        for x in sum2:
            y = target - x
            if y not in sum2:
                continue
            for i, j in sum2[x]:
                for k, l in sum2[y]:
                    idxs = set((i, j, k, l))
                    if len(idxs) != 4:
                        continue
                    vals = map(nums.__getitem__, idxs)
                    quads.add(tuple(sorted(vals)))
        return list(quads)

