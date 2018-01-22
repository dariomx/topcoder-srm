"""
Python3 solution with O(n*log(n)) time and space

We can hash all numbers (and save their positions), in order to do a second
pass and validate for each x where the values x-k or x+k do exist in such hash.
If they do we add the sorted pair into a set, so we do not count duplicates (
I suspect that this set can be eliminated, but did not have time to do it).
The saved index is to ensure we do not compare elements with themselves (for
odd cases like k=0).

Though worst cases will have a nested loop cost of O(log(n)), in practice
this is likely to remain O(1); hence this may have a practical complexity
(average?) of O(n).

"""

class Solution:
    def findPairs(self, nums, k):
        if k < 0:
            return 0
        n = len(nums)
        pos = dict()
        for i in range(n):
            pos[nums[i]] = i
        pairs = set()
        for i in range(n):
            x = nums[i]
            for y in (x-k, x+k):
                if y in pos and i != pos[y]:
                    pairs.add(tuple(sorted((x, y))))
        return len(pairs)