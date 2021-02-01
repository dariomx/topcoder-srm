from collections import deque, defaultdict
from itertools import chain
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        idx = defaultdict(deque)
        for i, x in enumerate(arr):
            idx[x].appendleft(i)
        queue = deque([(0, 0)])
        visited = {0}
        n = len(arr)
        while queue:
            node, steps = queue.popleft()
            if node == n-1:
                return steps
            for nei in chain(idx[arr[node]], (node-1, node+1)):
                if nei in visited:
                    continue
                if nei != node and 0 <= nei < n:
                    visited.add(nei)
                    queue.append((nei, steps+1))

# main
arr = [7] * 49999 + [11]
print(Solution().minJumps(arr))
