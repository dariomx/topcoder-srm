class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ans = ''
        P = ''
        cnt = 0
        for c in S:
            if c == '(':
                cnt += 1
            else:
                cnt -= 1
            P += c
            if cnt == 0:
                ans += P[1:-1]
                P = ''
        return ans