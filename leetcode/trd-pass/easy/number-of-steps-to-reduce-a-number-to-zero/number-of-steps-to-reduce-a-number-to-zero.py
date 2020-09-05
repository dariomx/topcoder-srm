class Solution:
    def numberOfSteps (self, num: int) -> int:
        ans = 0
        while num > 0:
            q, r = divmod(num, 2)
            if r == 0:
                num //= 2
            else:
                num -= 1
            ans += 1
        return ans