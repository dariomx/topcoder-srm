class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        equiv = defaultdict(list)
        for i, (x, y) in enumerate(dominoes):
            if y < x:
                x, y = y, x
            equiv[x, y].append(i)
        ans = 0
        for ix in equiv.values():
            n = len(ix)
            ans += n * (n-1) // 2
        return ans