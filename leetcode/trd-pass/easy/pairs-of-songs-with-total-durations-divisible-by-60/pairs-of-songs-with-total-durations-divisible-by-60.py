class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt = Counter(time)
        ans = 0
        for t, n in cnt.items():
            for k in range(1, 17):
                u = k * 60 - t
                if u == t:
                    ans += n * (n - 1) // 2
                else:
                    m = cnt.get(u, 0)
                    ans += n * m / 2
        return int(ans)
