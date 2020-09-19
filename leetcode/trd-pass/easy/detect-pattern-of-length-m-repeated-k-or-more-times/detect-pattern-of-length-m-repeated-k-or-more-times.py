class Solution:
    def isPattern(self, arr, i, m, k):
        for t in range(1, k):
            for j in range(m):
                if arr[i + t * m + j] != arr[i + j]:
                    return False
        return True

    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        for i in range(n - m * k + 1):
            if self.isPattern(arr, i, m, k):
                return True
        return False
