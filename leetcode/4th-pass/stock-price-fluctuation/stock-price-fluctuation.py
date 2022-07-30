from sortedcontainers import SortedSet

class StockPrice:
    
    def __init__(self):
        self._series = dict()
        self._cnt = defaultdict(lambda: 0)
        self._prices = SortedSet()
        self._max_time = None
        self._max_price = None
        self._min_price = None
        self._cur_price = None
        
    def update(self, timestamp: int, price: int) -> None:
        if self._cur_price is None:
            self._series[timestamp] = price
            self._cnt[price] = 1
            self._prices.add(price)
            self._max_time = timestamp
            self._max_price = self._min_price = self._cur_price = price
        else:
            old_price = self._series.get(timestamp, None)
            if old_price is not None:
                self._cnt[old_price] -= 1
                if self._cnt[old_price] == 0:
                    self._prices.remove(old_price)
            self._series[timestamp] = price
            self._cnt[price] += 1
            self._prices.add(price)
            self._max_time  = max(self._max_time, timestamp)                                    
            self._max_price = next(self._prices.__reversed__())
            self._min_price = next(self._prices.__iter__())
            self._cur_price = self._series[self._max_time]

    def current(self) -> int:
        return self._cur_price

    def maximum(self) -> int:
        return self._max_price

    def minimum(self) -> int:
        return self._min_price

