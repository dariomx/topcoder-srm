# not mine, saw stack idea on phorum

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        ans = deque()
        n = len(prices)
        for i in reversed(range(n)):
            while stack and stack[-1] > prices[i]:
                stack.pop()
            p = prices[i]
            if stack:
                p -= stack[-1]
            ans.appendleft(p)
            stack.append(prices[i])
        return ans