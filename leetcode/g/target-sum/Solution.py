from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

class Solution(object):
    def findTargetSumWays(self, nums, t):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        s = sum(nums)
        excess = s - t
        if excess < 0:
            return 0
        elif excess == 0:
            return 1
        ways = 0
        lt = [x for x in nums if x <= excess]
        for comb in powerset(lt):
            if sum(comb) == excess:
                ways += 1
        return ways