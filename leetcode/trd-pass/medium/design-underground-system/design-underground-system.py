# mine but pop suggestion from editorial (better to remove user, i guess
# as it is as expensive as fetching? ... at least in theory)

class UndergroundSystem:
    def __init__(self):
        self.sum = defaultdict(lambda: 0)
        self.cnt = defaultdict(lambda: 0)
        self.cin = dict()

    def checkIn(self, id: int, src: str, start: int) -> None:
        self.cin[id] = (src, start)

    def checkOut(self, id: int, dst: str, end: int) -> None:
        src, start = self.cin.pop(id)
        elapsed = end - start
        self.sum[src, dst] += elapsed
        self.cnt[src, dst] += 1

    def getAverageTime(self, src: str, dst: str) -> float:
        return self.sum[src, dst] / self.cnt[src, dst]
