class Solution:
    def distributeCandies(self, candies: int, n: int) -> List[int]:
        ans = [0] * n
        base = -n
        while candies > 0:
            base += n
            for i in range(n):
                c_i = base + (i + 1)
                if c_i > candies:
                    ans[i] += candies
                    candies = 0
                    break
                else:
                    ans[i] += c_i
                    candies -= c_i
        return ans
