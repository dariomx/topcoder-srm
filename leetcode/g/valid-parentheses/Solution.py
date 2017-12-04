class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        inv = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c in inv:
                if not stack or stack.pop() != inv[c]:
                    return False
            else:
                stack.append(c)
        return not stack
