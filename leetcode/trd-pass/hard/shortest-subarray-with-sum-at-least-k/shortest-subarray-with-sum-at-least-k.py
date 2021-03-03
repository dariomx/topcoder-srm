class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        n = len(A)
        heap = []
        psum = 0
        ans = inf
        for j, x in enumerate(A):
            psum += x
            if psum >= K:
                ans = min(ans, j+1)
            while heap and psum - heap[0][0] >= K:
                _, i = heappop(heap)
                ans = min(ans, j - i)
            heappush(heap, (psum, j))
        return ans if ans < inf else -1
