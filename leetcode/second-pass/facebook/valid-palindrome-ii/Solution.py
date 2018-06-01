class Solution:
    def validPalindrome(self, s):
        n = len(s)
        stack = [(0, n-1, False)]
        while stack:
            i, j, mdel = stack.pop()
            if i == j or j+1 == i:
                return True
            if s[i] == s[j]:
                stack.append((i+1, j-1, mdel))
            elif not mdel:
                stack.append((i+1, j, True))
                stack.append((i, j-1, True))
        return False