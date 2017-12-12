class Solution(object):
    def getBit(self, x, i):
        return (x & (1 << i)) >> i

    def countSeqOnes(self, x):
        cnt = 0
        for i in xrange(7, -1, -1):
            if self.getBit(x, i) == 1:
                cnt += 1
            else:
                break
        return cnt

    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(data):
            if self.getBit(data[i], 7) == 1:
                cnt = self.countSeqOnes(data[i])
                if not (2 <= cnt <= 4):
                    return False
                try:
                    for j in xrange(i + 1, i + cnt):
                        if self.getBit(data[j], 7) != 1 or \
                                        self.getBit(data[j], 6) != 0:
                            return False
                except IndexError:
                    return False
                i += cnt
            else:
                i += 1
        return True


data = [197, 130, 1]
print(Solution().validUtf8(data))
