class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda p: p[0])

        n = len(properties)
        maxpos_x = defaultdict(lambda: -inf)
        maxval_y = [-inf] * n
        maxval_y[n-1] = properties[n-1][1]
        for i in reversed(range(n-1)):
            x, y = properties[i]
            maxpos_x[x] = max(i, maxpos_x[x])
            maxval_y[i] = max(y, maxval_y[i+1])
        x, _ = properties[-1]
        maxpos_x[x] = max(n-1, maxpos_x[x])

        ans = 0
        for i, (x, y) in enumerate(properties[:-1]):
            j = maxpos_x[x]
            if j+1 < n and y < maxval_y[j+1]:
                ans += 1
        return ans
