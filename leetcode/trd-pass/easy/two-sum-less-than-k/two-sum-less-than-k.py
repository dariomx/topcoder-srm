class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        i = bisect_left(A, K)
        if i == 0 and A[i] == K:
            return -1
        elif i == len(A) or A[i] > K:
            i -= 1
        ans = -1
        for j in range(i, -1, -1):
            target = K - A[j] - 1
            l = bisect_right(A, target, hi=j)
            if l == j:
                l = j - 1
            elif (A[l] > target and l > 0):
                l -= 1
            if 0 <= l < j and A[l] + A[j] < K:
                ans = max(ans, A[l] + A[j])
        return ans
