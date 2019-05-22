class Solution:
    def binSearch(self, arr, x):
        n = len(arr)
        start = 0
        end = n - 1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid].start <= x <= arr[mid].end:
                return mid, 0
            elif x < arr[mid].start:
                if mid == start:
                    return mid, -1
                else:
                    end = mid - 1
            else:
                if mid == end:
                    return mid, +1
                else:
                    start = mid + 1
        raise ValueError("could not end binary search for " + str(x))

    def insertVal(self, arr, x):
        i, dir = self.binSearch(arr, x)
        if dir < 0:
            arr = arr[:i] + [Interval(x, x)] + arr[i:]
        elif dir > 0:
            arr = arr[:i + 1] + [Interval(x, x)] + arr[i + 1:]
            i += 1
        return arr, i

    def merge(self, i1, i2):
        return Interval(min(i1.start, i2.start), max(i1.end, i2.end))

    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        intervals, i = self.insertVal(intervals, newInterval.start)
        intervals, j = self.insertVal(intervals, newInterval.end)
        middle = self.merge(intervals[i], intervals[j])
        return intervals[:i] + [middle] + intervals[j + 1:]
