class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        start, end = 0, len(A) - 1
        ans = inf
        while start <= end:
            mid = (start + end) // 2
            if mid <= A[mid]:
                if mid == A[mid]:
                    ans = min(ans, mid)
                end = mid - 1
            else:
                start = mid + 1
        return -1 if ans == inf else ans