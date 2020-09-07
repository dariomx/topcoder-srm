class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        ans = 0
        for x in arr1:
            i = min(bisect_left(arr2, x), len(arr2)-1)
            dist = abs(arr2[i] - x)
            if i-1 >= 0:
                dist = min(dist, abs(arr2[i-1] - x))
            if i+1 < len(arr2):
                dist = min(dist, abs(arr2[i+1] - x))
            if dist > d:
                ans += 1
        return ans