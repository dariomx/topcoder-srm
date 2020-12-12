class Solution:
    def trimMean(self, arr: List[int]) -> float:
        S, n = sum(arr), len(arr)
        fivep = int(n * 0.05)
        heapify(arr)
        for _ in range(fivep):
            S -= heappop(arr)
        for i in range(n - fivep):
            arr[i] *= -1
        heapify(arr)
        for _ in range(fivep):
            S -= -heappop(arr)
        return S / (n - 2 * fivep)
