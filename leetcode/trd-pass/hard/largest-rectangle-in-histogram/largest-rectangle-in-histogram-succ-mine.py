class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def dedup(A):
            D, cnt, prev = [], [], None
            for x in A:
                if x == prev:
                    cnt[-1] += 1
                else:
                    D.append(x)
                    cnt.append(1)
                    prev = x
            return D, cnt

        def prefixSum(A):
            psum = [0] * len(A)
            for i in range(len(A)):
                psum[i] = psum[i - 1] + A[i]
            return psum

        def rangeWidth(start, end):
            return psWidth[end] - psWidth[start] + width[start]

        def getMin(start, end):
            minv, mini = inf, None
            for i in range(start, end + 1):
                if heights[i] < minv:
                    minv, mini = heights[i], i
            return minv, mini

        def search(start, end):
            nonlocal ans
            if start > end:
                return 0
            minh, i = getMin(start, end)
            ans = max(ans, rangeWidth(start, end) * minh)
            search(start, i - 1)
            search(i + 1, end)

        # main
        heights, width = dedup(heights)
        psWidth = prefixSum(width)
        ans = 0
        search(0, len(heights) - 1)
        return ans
