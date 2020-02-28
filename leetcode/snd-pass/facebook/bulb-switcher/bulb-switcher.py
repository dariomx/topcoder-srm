class Solution:
    def bulbSwitch(self, n: int) -> int:
        ans = 0
        c = 0
        even = 2
        while True:
            c += 1
            if c > n:
                break
            ans += 1
            c += even
            even += 2
        return ans
