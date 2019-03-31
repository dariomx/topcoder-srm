# I think editorial solution #1 is not correct, cause there could
# be cases where the sizes which add up to the half we look for,
# are not contiguous

class Solution(object):
    def reorganizeString(self, S):
        N = len(S)
        A = []
        for c, x in sorted((S.count(x), x) for x in set(S)):
            if c > (N+1)//2: return ""
            A.extend(c * x)
        ans = [None] * N
        ans[::2], ans[1::2] = A[N//2:], A[:N//2]
        return "".join(ans)

S = "abbcccdddd"
print(Solution().reorganizeString(S))