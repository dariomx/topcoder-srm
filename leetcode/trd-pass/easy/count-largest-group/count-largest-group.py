class Solution:
    def countLargestGroup(self, n: int) -> int:
        gsize = defaultdict(lambda: 0)
        max_size = 0
        ans = 0
        for x in range(1, n+1):
            sx = sum(map(int, str(x)))
            gsize[sx] += 1
            if gsize[sx] > max_size:
                max_size = gsize[sx]
                ans = 1
            elif gsize[sx] == max_size:
                ans += 1
        return ans