# not proud of this piece of shait, the idea is not even mine (too hint1)
# looks like taking the global minimum was not really needed; taking
# it locally was good enough ... which lead to the kinda stairs pattern
# i was trying to cook ... i failed to see the rule of taking the local
# minimum of the current point among dimensions, shame on me.

from heapq import heapify, heappop, heappush
from typing import List

ROW = 0
COL = 1


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[
        List[int]]:
        n, m = len(rowSum), len(colSum)
        pos = {ROW: {i: set(range(m)) for i in range(n)},
               COL: {j: set(range(n)) for j in range(m)}}
        used = set()
        curSum = {ROW: {i: rowSum[i] for i in range(n)},
                  COL: {j: colSum[j] for j in range(m)}}
        minHeap = [(s, (i, ROW)) for (i, s) in enumerate(rowSum)] + \
                  [(s, (j, COL)) for (j, s) in enumerate(colSum)]
        heapify(minHeap)
        ans = [[0] * m for _ in range(n)]
        while minHeap:
            s, (i, dim) = heappop(minHeap)
            if s == 0:
                used.add((i, dim))
                continue
            elif s != curSum[dim][i]:
                continue
            otherDim = COL if dim == ROW else ROW
            j = pos[dim][i].pop()
            while (j, otherDim) in used:
                j = pos[dim][i].pop()
            used.add((i, dim))
            if dim == ROW:
                ans[i][j] = s
            else:
                ans[j][i] = s
            pos[otherDim][j].remove(i)
            curSum[dim][i] -= s
            curSum[otherDim][j] -= s
            if curSum[otherDim][j] >= 0:
                heappush(minHeap, (curSum[otherDim][j], (j, otherDim)))
        return ans

# main
rowSum = [33,26,9,12,25,18,19,30,34]
colSum = [25,126,8,13,34]
print(Solution().restoreMatrix(rowSum, colSum))
