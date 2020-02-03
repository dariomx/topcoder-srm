class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        abs_start = 0
        for end, c in enumerate(s):
            if c == '(':
                stack.append(end)
            elif stack:
                stack.pop()
                if stack:
                    start = stack[-1] + 1
                else:
                    start = abs_start
                ans = max(ans, end - start + 1)
            else:
                abs_start = end + 1
        return ans
