class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        coeff, ans, psum = 0, 0, 0
        for x in sorted(satisfaction, reverse=True):
            coeff += psum + x
            ans = max(ans, coeff)
            psum += x
        return ans
