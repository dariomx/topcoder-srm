from sortedcontainers import SortedList

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = [[0] * n for _ in range(m)]
        left, right = SortedList([-inf]), SortedList([-inf])
        
        for j in range(n):
            dp[m-1][j] = points[m-1][j]
            right.add(points[m-1][j] - j)
      
        for i in reversed(range(m-1)):
            new_left, new_right = SortedList([-inf]), SortedList([-inf])
            for j in range(n):
                x = dp[i+1][j]
                right.remove(x - j)                
                dp[i][j] = points[i][j] + max(left[-1] + (n-1-j), x, right[-1] + j)
                left.add(x - (n-1-j))
                new_right.add(dp[i][j] - j)
            left, right = new_left, new_right

        return max(dp[0])
