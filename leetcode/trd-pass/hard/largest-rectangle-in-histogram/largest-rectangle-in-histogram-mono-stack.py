# not my idea, but my version a phorum post with the winner soln (monotonic stack)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0) # sentinel to avoid second loop
        stack, ans = [], 0
        for i in range(len(heights)):
            start, end = i, i - 1
            while stack and stack[-1][0] >= heights[i]:
                hmin, start = stack.pop()
                ans = max(ans, (end - start + 1) * hmin)
            stack.append((heights[i], start))
        return ans