class Solution:
    def area(self, v, u):
        dot = v[0] * u[0] + v[1] * u[1]
        norm_v = sqrt(v[0] ** 2 + v[1] ** 2)
        norm_u = sqrt(u[0] ** 2 + u[1] ** 2)
        theta = math.acos(dot / (norm_v * norm_u))
        if math.isclose(theta, math.pi / 2):
            return norm_v * norm_u
        else:
            return inf

    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        pset = {(x, y) for (x, y) in points}
        n = len(points)
        ans = inf
        for i in range(n):
            p = points[i]
            for j in range(i + 1, n):
                q = points[j]
                v = q[0] - p[0], q[1] - p[1]
                for k in range(j + 1, n):
                    r = points[k]
                    u = r[0] - p[0], r[1] - p[1]
                    s = p[0] + (v[0] + u[0]), p[1] + (v[1] + u[1])
                    if s in pset:
                        ans = min(ans, self.area(v, u))
        return ans if ans < inf else 0