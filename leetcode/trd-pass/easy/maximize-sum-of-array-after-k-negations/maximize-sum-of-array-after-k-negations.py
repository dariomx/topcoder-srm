# this would had been better with a min-heap, but hey, at least got out
# of the dp-falacy

from operator import itemgetter

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        n = len(A)
        A.sort()
        i = 0
        while K > 0 and i < n and A[i] < 0:
            A[i] *= -1
            i += 1
            K -= 1
        if K % 2 == 1:
            j, _ = min(enumerate(A), key=itemgetter(1))
            A[j] *= -1
        return sum(A)