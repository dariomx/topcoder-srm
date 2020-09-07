class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        ans = -1
        for x in arr:
            if cnt[x] == x:
                ans = max(ans, x)
        return ans