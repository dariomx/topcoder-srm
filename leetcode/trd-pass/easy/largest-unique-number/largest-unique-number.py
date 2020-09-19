class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        return max((x for x, k in Counter(A).items() if k == 1), default=-1)
