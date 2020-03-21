class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        for c in S:
            if c == ')' and stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(c)
        return len(stack)
