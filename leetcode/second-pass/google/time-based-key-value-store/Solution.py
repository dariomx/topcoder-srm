from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.vals = defaultdict(lambda: [])

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.vals[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.vals:
            return ""
        V = self.vals[key]
        start, end = 0, len(V)-1
        while start <= end:
            mid = (start + end)//2
            if V[mid][0] > timestamp:
                end = mid - 1
            elif mid == end or V[mid+1][0] > timestamp:
                return V[mid][1]
            else:
                start = mid + 1
        return ""
