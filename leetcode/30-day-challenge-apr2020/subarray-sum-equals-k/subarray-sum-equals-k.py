class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = dict()
        psum = 0
        ans = 0
        for x in nums:
            psum += x
            if psum == k:
                ans += 1
            ans += cnt.get(psum - k, 0)
            cnt[psum] = cnt.get(psum, 0) + 1
        return ans