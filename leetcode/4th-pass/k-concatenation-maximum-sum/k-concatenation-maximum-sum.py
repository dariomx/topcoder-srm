class Solution:
    def maxSubSum(self, arr: List[int]) -> int:
        psum = 0
        min_psum = inf
        max_ssum = -inf
        for x in arr:
            psum += x
            max_ssum = max(max_ssum, psum, psum - min_psum)
            min_psum = min(min_psum, psum)
        return max_ssum, psum
    
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        max_ssum, gain = self.maxSubSum(arr)
        if k == 1:
            ans = max_ssum
        else:
            max_ssum2, _ = self.maxSubSum(arr + arr)
            ans = max(max_ssum, max_ssum + (k-1) * gain, max_ssum2)
        return ans % (10**9 + 7) if ans >= 0 else 0
    
