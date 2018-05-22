class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        rm_idx = lambda i: num[:i] + num[i + 1:]
        for _ in xrange(k):
            if len(num) > 1 and num[0] != '0' and num[1] == '0':
                num = num[1:]
                while len(num) > 0 and num[0] == '0':
                    num = num[1:]
            else:
                i = min(xrange(len(num)), key=rm_idx)
                num = rm_idx(i)
            if num == '':
                num = '0'
        return num
