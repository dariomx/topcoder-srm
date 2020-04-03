from sortedcontainers import SortedList

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        idx = SortedList(range(n))
        sht = sorted(range(n), key=lambda i: height[i])
        for i in sht[:-1]:
            idx.remove(i)
            width = max(abs(i - idx[0]), abs(i - idx[-1]))
            ans = max(ans, height[i] * width)
        return ans