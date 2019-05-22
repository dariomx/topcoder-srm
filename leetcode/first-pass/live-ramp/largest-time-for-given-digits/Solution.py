from itertools import permutations as perm


class Solution(object):
    def largestTimeFromDigits(self, A):
        ans = ""
        tmax = -1
        for p in perm(A):
            hour = p[0] * 10 + p[1]
            minute = p[2] * 10 + p[3]
            if 0 <= hour < 24 and 0 <= minute < 60:
                tmins = hour * 60 + minute
                if tmins > tmax:
                    tmax = tmins
                    ans = (hour, minute)
        return ("%02d:%02d" % ans) if ans else ans

