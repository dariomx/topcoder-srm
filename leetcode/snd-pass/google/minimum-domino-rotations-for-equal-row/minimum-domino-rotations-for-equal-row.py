from collections import Counter, defaultdict
from math import inf


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n, k = len(A), 6
        cnt_A = [0] * (k + 1)
        cnt_B = [0] * (k + 1)
        mules = [0] * (k + 1)
        for i in range(n):
            a, b = A[i], B[i]
            cnt_A[a] += 1
            cnt_B[b] += 1
            if a == b:
                mules[a] += 1
        ans = inf
        for x in range(1, k + 1):
            if cnt_A[x] + cnt_B[x] - 2 * mules[x] == n - mules[x]:
                ans = min(ans, min(cnt_A[x], cnt_B[x]) - mules[x])
        return -1 if ans == inf else ans

