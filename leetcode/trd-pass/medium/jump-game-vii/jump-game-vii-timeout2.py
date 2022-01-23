class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        heap = [0]
        while heap:
            i = -heappop(heap)
            if i == len(s) - 1:
                return True
            for j in range(i + minJump, min(i + maxJump, len(s) - 1) + 1):
                if s[j] == '0':
                    heappush(heap, -j)
        return False