class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        heapify(arr)
        totw = 0
        ans = 0
        while arr:
            w = heappop(arr)
            if totw + w > 5000:
                break
            else:
                totw += w
                ans += 1
        return ans
