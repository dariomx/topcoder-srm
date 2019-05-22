# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        merged = []
        ikey = lambda i: (i.start, i.end)
        intvs = sorted(intervals, key=ikey)
        a, b = ikey(intvs[0])
        for i in intvs[1:]:
            c, d = ikey(i)
            if a <= c <= b:
                a = min(a, c)
                b = max(b, d)
            else:
                merged.append([a, b])
                a, b = c, d
        merged.append([a, b])
        return merged
