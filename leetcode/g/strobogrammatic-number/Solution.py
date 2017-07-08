class Solution(object):
    def __init__(self):
        self.inv = {'6': '9', '9': '6', '1': '1', '8': '8', '0': '0'}

    def validPos(self, num, n, i):
        return num[i] in self.inv and \
               num[n - 1 - i] in self.inv and \
               num[i] == self.inv[num[n - 1 - i]]

    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i in xrange(n / 2 + n % 2):
            if not self.validPos(num, n, i):
                return False
        return True
