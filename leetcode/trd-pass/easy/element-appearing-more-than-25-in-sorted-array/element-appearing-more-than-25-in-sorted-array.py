class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        qrt = len(arr) // 4
        cnt = 0
        prev = None
        for x in arr:
            if x == prev:
                cnt += 1
            else:
                cnt = 1
                prev = x
            if cnt > qrt:
                return x
