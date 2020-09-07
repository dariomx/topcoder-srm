class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        for i in range(1, n-1):
            delta_fwd = arr[i+1] - arr[i]
            delta_bwd = arr[i] - arr[i-1]
            if abs(delta_bwd) < abs(delta_fwd):
                return arr[i] + delta_bwd
            elif abs(delta_bwd) > abs(delta_fwd):
                return arr[i] - delta_fwd
        return arr[0]
