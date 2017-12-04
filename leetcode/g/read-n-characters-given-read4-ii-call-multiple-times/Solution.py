# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        m = 0
        j = 0
        buf4 = [''] * 4
        while m < n:
            k = read4(buf4)
            for i in xrange(k):
                if j < n:
                    buf[j] = buf4[i]
                    j += 1
            else:
                break
            m += k
        return m
