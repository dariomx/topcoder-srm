# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        START = 1
        END = 0
        time = []
        for iv in intervals:
            time.append((iv.start, START))
            time.append((iv.end, END))
        time.sort()
        overlap = 0
        max_overlap = 0
        for (t, kind) in time:
            if kind == START:
                overlap += 1
                max_overlap = max(max_overlap, overlap)
            else:
                overlap -= 1
        return max_overlap
