# inspired by editorial soln (why slower than recursive-brute force?)

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [('', 0)]
        for c in s:
            if c == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return ''.join(c * k for (c, k) in stack)
