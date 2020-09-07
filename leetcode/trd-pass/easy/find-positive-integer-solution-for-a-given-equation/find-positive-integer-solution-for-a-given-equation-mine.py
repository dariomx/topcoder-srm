"""
Could not make it better than the O(n log n), but kinda felt this was
not optimum.
"""


class Solution:
    def binSearch(self, f, z):
        start, end = 1, 1000
        while start <= end:
            mid = (start + end) // 2
            fmid = f(mid)
            if z == fmid:
                return mid
            elif z < fmid:
                end = mid - 1
            else:
                start = mid + 1
        return None

    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[
        List[int]]:
        ans = []
        for x in range(1, 1001):
            f = lambda y: customfunction.f(x, y)
            y = self.binSearch(f, z)
            if y:
                ans.append((x, y))
        return ans