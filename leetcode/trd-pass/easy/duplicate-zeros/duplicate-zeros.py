class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        zeros = [0] * n
        cnt = 0
        for i in range(n):
            zeros[i] = cnt
            if arr[i] == 0:
                cnt += 1
        for i in range(n - 1, -1, -1):
            j = i + zeros[i]
            if j < n:
                arr[j] = arr[i]
                if arr[i] == 0 and j + 1 < n:
                    arr[j + 1] = arr[i]
