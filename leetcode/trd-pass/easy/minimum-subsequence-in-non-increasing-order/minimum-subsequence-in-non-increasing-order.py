class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        n = len(nums)
        tsum = 0
        for i in range(n):
            tsum += nums[i]
            nums[i] *= -1
        half = tsum // 2
        heapify(nums)
        psum = 0
        ans = []
        while psum <= half:
            x = -heappop(nums)
            ans.append(x)
            psum += x
        return ans