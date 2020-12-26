class Solution:
    def candy(self, R: List[int]) -> int:
        n = len(R)
        left = [1] * n
        for i in range(1, n):
            if R[i - 1] < R[i]:
                left[i] += left[i - 1]
        right = [1] * n
        ans = max(left[n - 1], right[n - 1])
        for i in reversed(range(n - 1)):
            if R[i] > R[i + 1]:
                right[i] += right[i + 1]
            ans += max(left[i], right[i])
        return ans
