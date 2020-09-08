class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        cnt = defaultdict(list)
        for i in range(m):
            c = 0
            for j in range(n):
                if mat[i][j] == 0:
                    break
                c += 1
            cnt[c].append(i)
        ans = []
        for c in range(n+1):
            if c in cnt:
                ans += cnt[c]
            if len(ans) >= k:
                break
        return ans[:k]