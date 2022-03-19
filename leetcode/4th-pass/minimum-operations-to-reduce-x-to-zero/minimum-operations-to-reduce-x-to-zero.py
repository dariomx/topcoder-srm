class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        postsum = [0] * n
        postsum[n-1] = nums[n-1]
        for i in reversed(range(n-1)):
            postsum[i] = nums[i] + postsum[i+1]
            
        postlt = defaultdict(lambda: -inf)
        for i, s in enumerate(postsum):
            postlt[s] = max(i, postlt[s])
            
        j = postlt[x]
        if j != -inf:
            ans = n-j
        else:
            ans = inf
                               
        presum = 0
        for i in range(n):
            presum += nums[i]
            if presum == x:
                ans = min(ans, i+1)
            j = postlt[x - presum]
            if j == -inf or j <= i:
                continue
            ans = min(ans, (i+1) + (n-j))
            
        return ans if ans < inf else -1
