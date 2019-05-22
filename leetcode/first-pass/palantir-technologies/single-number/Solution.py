class Solution:
    def singleNumber(self, nums):
        S = sum(nums)
        cand = set()
        for y in nums:
            q, r = divmod(S-y, 2)
            if r == 0 and 2*q + y == S:
                if y in cand:
                    cand.remove(y)
                else:
                    cand.add(y)
        return cand.pop()
