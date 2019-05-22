class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda i: i.start)
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            last = ans[-1]
            curr = intervals[i]
            if curr.start <= last.end:
                ans.pop()
                ans.append(Interval(last.start, max(curr.end, last.end)))
            else:
                ans.append(curr)
        return ans