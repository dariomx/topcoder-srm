from heapq import heapify, heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapify(stones)
        while len(stones) > 1:
            x, y = heappop(stones), heappop(stones)
            x, y = abs(x), abs(y)
            if x != y:
                heappush(stones, min(x, y) - max(x, y))
        return abs(stones[0]) if stones else 0
