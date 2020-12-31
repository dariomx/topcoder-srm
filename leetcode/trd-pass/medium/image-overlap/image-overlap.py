# my version of fst editorial soln

class Solution:
    def shift_cnt(self, dx, dy, img1, img2):
        n = len(img1)
        cnt = 0
        for x in range(n):
            nx = x + dx
            for y in range(n):
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < n and img1[x][y] == 1:
                    cnt += int(img1[x][y] == img2[nx][ny])
        return cnt

    def largestOverlap(self, img1: List[List[int]],
                       img2: List[List[int]]) -> int:
        n = len(img1)
        ans = 0
        for dx in range(-n, n + 1):
            for dy in range(-n, n + 1):
                ans = max(ans, self.shift_cnt(dx, dy, img1, img2))
        return ans