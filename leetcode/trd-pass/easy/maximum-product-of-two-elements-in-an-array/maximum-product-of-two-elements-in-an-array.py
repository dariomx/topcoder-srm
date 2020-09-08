class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lst, sndLst = -inf, -inf
        for x in nums:
            if x > lst:
                sndLst = lst
                lst = x
            elif x > sndLst:
                sndLst = x
        return (lst - 1) * (sndLst - 1)

