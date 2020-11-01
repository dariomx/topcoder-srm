class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = sorted((x for x, _ in points))
        prev = xs[0]
        ans = 0
        for x in xs:
            width = x - prev
            ans = max(ans, width)
            prev = x
        return ans
