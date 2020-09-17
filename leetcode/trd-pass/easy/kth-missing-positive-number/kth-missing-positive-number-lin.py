class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k < arr[0]:
            return k
        elif arr[n - 1] - arr[0] + 1 == n:
            return arr[n - 1] + k
        else:
            k -= arr[0] - 1
            for i in range(1, n):
                for x in range(arr[i - 1] + 1, arr[i]):
                    k -= 1
                    if k == 0:
                        return x
            if k > 0:
                return arr[n - 1] + k
