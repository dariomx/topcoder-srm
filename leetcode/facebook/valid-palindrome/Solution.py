class Solution(object):
    def isPalindrome(self, s):
        s = [c for c in s.lower() if c.isalpha() or c.isnumeric()]
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                return False
        return True
