from math import inf

A = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,1,0],[1,1,0,0,0,0,1,0,0],[0,0,0,1,1,1,0,0,0]]

n, m = len(A), len(A[0])
ps = []
for i in range(n):
    for j in range(m):
        if A[i][j] == 1:
            ps.append((i, j))

ans = [inf, None]
for i in range(n):
    for j in range(m):
        d = 0
        for p in ps:
            d += abs(p[0] - i) + abs(p[1] - j)
        print(i, j, d)
        if d < ans[0]:
            ans = [d, (i, j)]
print(ans)

