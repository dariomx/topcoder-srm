# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from collections import defaultdict


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        time = defaultdict(lambda: 0)
        for iv in intervals:
            for slot in xrange(iv.start, iv.end):
                time[slot] += 1
        max_rooms = 0
        for cnt in time.itervalues():
            max_rooms = max(max_rooms, cnt)
        return max_rooms
