def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'

    class K:
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0

    return K


class Solution(object):
    def trim_zeros(self, num):
        while len(num) > 0 and num[0] == '0':
            num = num[1:]
        if num == '':
            num = '0'
        return num

    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        def cmp_idx(i, j):
            if i > j:
                inv = -1
                i, j = j, i
            else:
                inv = 1
            ret = lambda c: inv * c
            cmp = 0
            for k in xrange(i, j):
                diff = ord(num[k + 1]) - ord(num[k])
                if diff < 0:
                    cmp = ret(-1)
                    break
                elif diff > 0:
                    cmp = ret(+1)
                    break
            # print("cmp(%d,%d,%d) = %d" % (i, j, inv, cmp))
            return cmp
            #

        cnt = 0
        while cnt < k:
            # print("before " + num)
            if len(num) > 1 and num[0] != '0' and num[1] == '0':
                num = num[1:]
                cnt += 1
                num = self.trim_zeros(num)
            if cnt < k:
                i = min(xrange(len(num)), key=cmp_to_key(cmp_idx))
                num = num[:i] + num[i + 1:]
                cnt += 1
                # print("after " + num)
        num = self.trim_zeros(num)
        return num
