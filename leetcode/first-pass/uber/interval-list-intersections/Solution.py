class Solution:
    def getIntersect(self, x, y):
        start = max(x.start, y.start)
        end = min(x.end, y.end)
        if x.start <= start <= y.end and y.start <= end <= y.end:
            return Interval(start, end)
        else:
            return None

    def intervalIntersection(self, A: List[Interval], B: List[Interval]) -> \
    List[Interval]:
        ans = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            inter = self.getIntersect(A[i], B[j])
            if inter is not None:
                ans.append(inter)
            if A[i].end < B[j].end:
                i += 1
            elif B[j].end < A[i].end:
                j += 1
            else:
                i += 1
                j += 1
        return ans