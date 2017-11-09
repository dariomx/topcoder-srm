from collections import deque


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        rm_idx = lambda s, i: s[:i] + s[i + 1:]
        stack = deque(num.split('0'))
        while k > 0 and stack:
            s = stack.popleft()
            n = len(s)
            if n <= k:
                k -= n
            else:
                i = min(xrange(n), key=lambda j: rm_idx(s, j))
                s = rm_idx(s, i)
                stack.appendleft(s)
                k -= 1
        ret = ''
        n = len(stack)
        for i in xrange(n):
            ret += stack[i]
            if i < n - 1:
                ret += '0'
        return '0' if not ret else ret
