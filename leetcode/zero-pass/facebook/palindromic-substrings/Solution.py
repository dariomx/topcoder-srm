class Solution(object):
    def countSubstrings(self, s):
        n = len(s)
        stack = []
        for i in range(n):
            stack.append((i, i))
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                stack.append((i, i + 1))
        cnt = 0
        while stack:
            i, j = stack.pop()
            cnt += 1
            if i - 1 >= 0 and j + 1 < n and s[i - 1] == s[j + 1]:
                stack.append((i - 1, j + 1))
        return cnt

