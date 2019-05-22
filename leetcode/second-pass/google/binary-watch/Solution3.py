class Solution(object):
    def cnt_bits_on(self, x, n):
        cnt = 0
        for i in xrange(n):
            cnt += (x & (1 << i)) >> i
        return cnt

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num == 0:
            return ["0:00"]
        hrs_bits_on = dict()
        for h in xrange(12):
            hrs_bits_on[h] = self.cnt_bits_on(h, 4)
        min_bits_on = dict()
        for m in xrange(60):
            min_bits_on[m] = self.cnt_bits_on(m, 6)
        ans = []
        for h in xrange(12):
            for m in xrange(60):
                bits_on = hrs_bits_on[h]
                bits_on += min_bits_on[m]
                if bits_on == num:
                    ans.append("%d:%02d" % (h, m))
        return ans
