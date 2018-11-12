class Solution:
    def shortestToChar(self, S, C):
        n = len(S)
        ans = []
        last = None
        for i in range(n):
            if S[i] == C:
                last = i
            if last is None:
                ans.append(None)
            else:
                ans.append(i - last)
        last = None
        for i in reversed(range(n)):
            if S[i] == C:
                last = i
            if last is not None:
                if ans[i] is None:
                    ans[i] = last - i
                else:
                    ans[i] = min(ans[i], last - i)
        return ans
