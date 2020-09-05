class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        for x in range(1, n//2+1):
            ans.append(x)
            ans.append(-x)
        if n % 2 == 1:
            ans.append(0)
        return ans