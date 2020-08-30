# count-sort based soln, based on another's port seen in phorum (mine used
# regular sorts)

from math import inf

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n = 1001
        cnt1 = [0] * n
        in_arr2 = [False] * n
        max_x = -inf
        ans = []
        for x in arr1:
            cnt1[x] += 1
            max_x = max(max_x, x)
        for x in arr2:
            in_arr2[x] = True
            ans += [x] * cnt1[x]
        for x in range(max_x+1):
            if not in_arr2[x]:
                ans += [x] * cnt1[x]
        return ans
