class Solution:
    def knightDialer(self, N: int) -> int:
        R = 10**9 + 7
        graph = {1: [6,8],
                 2: [7,9],
                 3: [8,4],
                 4: [3,9,0],
                 5: [],
                 6: [1,7,0],
                 7: [6,2],
                 8: [3,1],
                 9: [4,2],
                 0: [6,4]}
        rec = [[0]*(N+1) for _ in range(10)]
        for d in range(10):
            rec[d][1] = 1
        for j in range(2, N+1):
            for d in range(10):
                rec[d][j] = \
                    sum((rec[nei][j-1] for nei in graph[d]))
        ans = sum((rec[d][N] for d in range(10)))
        return ans % R