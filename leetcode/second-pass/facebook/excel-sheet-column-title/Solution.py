class Solution:
    def convertToTitle(self, n):
        base = 26
        name = dict()
        for i in range(1, base + 1):
            name[i] = chr(ord('A') + i - 1)
        name[0] = 'Z'
        title = ""
        while n > 0:
            dig = n % base
            title = name[dig] + title
            n //= base
            if dig == 0:
                n -= 1
        return title
