class Solution:
    def typeStr(self, s):
        stack = []
        for c in s:
            if c == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return "".join(stack)

    def backspaceCompare(self, S, T):
        return self.typeStr(S) == self.typeStr(T)