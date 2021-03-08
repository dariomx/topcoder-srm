class Solution:
    def count(self, nums: list[int]) -> tuple[int, int]:
        prev = None
        cnt = 0
        maxCnt, totCnt = -inf, 0
        for x in chain(nums, [0]):
            if x == prev:
                cnt += 1
            else:
                if cnt > 0:
                    maxCnt = max(maxCnt, cnt)
                    totCnt += cnt
                cnt = 1
                prev = x
        return maxCnt, totCnt

    def canDivideIntoSubsequences(self, nums: List[int], K: int) -> bool:
        maxCnt, totCnt = self.count(nums)
        return (totCnt - maxCnt) // maxCnt >= (K-1)
