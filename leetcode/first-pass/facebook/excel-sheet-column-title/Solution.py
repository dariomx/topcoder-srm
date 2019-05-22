class Solution:
    def convertToTitle(self, n):
        k = 26
        title = ''
        while n > 0:
            n -= 1
            title = chr(ord('A') + n % k) + title
            n //= k
        return title
