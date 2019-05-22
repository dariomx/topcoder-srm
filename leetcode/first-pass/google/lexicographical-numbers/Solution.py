class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        k = len(str(n))
        pow10 = [1] * (k+1)
        ans = []
        for i in range(1, k+1):
            pow10[i] = pow10[i-1] * 10
            ans += list(range(pow10[i-1], min(n, pow10[i]-1)+1))
        ans.sort(key=str)
        return ans