class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda i: i.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True