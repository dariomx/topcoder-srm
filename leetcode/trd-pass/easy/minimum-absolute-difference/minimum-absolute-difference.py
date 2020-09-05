class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        prev = arr[0]
        min_dist = inf
        ans = []
        for x in arr[1:]:
            dist = abs(x - prev)
            if dist < min_dist:
                ans = [(prev, x)]
                min_dist = dist
            elif dist == min_dist:
                ans.append((prev, x))
            prev = x
        return ans