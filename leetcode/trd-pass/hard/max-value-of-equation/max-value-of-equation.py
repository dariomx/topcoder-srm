"""
I can see many people used the forward formulation, but for me it was easier to think
in the backwards one. If you are moving from right to left, and at each iteration
you name your reference x1, y1; then the best guy you can pair with is on the
right (no need to check left side due symmetry), and it is the one giving you maximum
y1 + y2 + abs(x1 - x2).

If we split the function above in two pieces, y1 + y2 and abs(x1 - x2), and remember that
x1 and y1 are constants for current iteration; we realize that both are increasing functions
respect to their respective parameters y2 and x2. Hence we want to pick the maximum value
of both variables together, which I think would be simply the max of their sum (aka y2 + x2),
over all the elements on the right of current reference (x1, y1).

Above may allow a more formal proof, but if you buy it, then we can apply the usual trick
of finding such best guy (x2, y2) on each iteration with a max-heap;  yielding the O(n log n)
solution that many other got with the forward-thinking approach.
"""

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        n = len(points)
        heap = []
        ans = -inf
        for i in reversed(range(n)):
            x1, y1 = points[i]
            while heap:
                _, j = heappop(heap)
                x2, y2 = points[j]
                dx = abs(x1 - x2)
                if dx <= k:
                    ans = max(ans, y1 + y2 + dx)
                    heappush(heap, (-(x2 + y2), j))
                    break
            heappush(heap, (-(x1 + y1), i))
        return ans
