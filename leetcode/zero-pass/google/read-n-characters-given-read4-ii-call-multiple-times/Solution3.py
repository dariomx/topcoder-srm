from collections import deque


# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.cache = deque()

    def read_file(self, buf, j, n):
        buf4 = [''] * 4
        k = 4
        while j < n and k == 4:
            k = read4(buf4)
            for i in xrange(k):
                if j < n:
                    buf[j] = buf4[i]
                    j += 1
                else:
                    self.cache.append(buf4[i])
        return j

    def read_cache(self, buf, n):
        j = 0
        while self.cache:
            if j < n:
                buf[j] = self.cache.popleft()
                j += 1
            else:
                break
        return j

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        m = self.read_cache(buf, n)
        if m < n:
            m = self.read_file(buf, m, n)
        return m
