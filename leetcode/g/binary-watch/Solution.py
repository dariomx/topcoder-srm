from itertools import permutations


class Solution(object):
    def bin2dec(self, arr, start, end):
        dec = 0
        pow2 = 1
        for i in xrange(end, start - 1, -1):
            dec += pow2 * arr[i]
            pow2 *= 2
        return dec

    def arr2time(self, arr):
        hrs = self.bin2dec(arr, 0, 3)
        min = self.bin2dec(arr, 4, 9)
        return "%d:%02d" % (hrs, min)

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num == 0:
            return ["0:00"]
        ans = []
        ini_arr = [0] * 10
        for i in xrange(0, num):
            ini_arr[i] = 1
        for arr in permutations(ini_arr):
            ans.append(self.arr2time(arr))
        return ans
