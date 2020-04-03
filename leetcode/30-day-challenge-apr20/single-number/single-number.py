# doing divisions to filter may be more expensive than the set log(n) lookup
class Solution:
    def singleNumber(self, nums):
        seen = set()
        for x in nums:
            if x in seen:
                seen.remove(x)
            else:
                seen.add(x)
        return seen.pop()