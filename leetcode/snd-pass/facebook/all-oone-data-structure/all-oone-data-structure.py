class AllOne:
    def __init__(self):
        self.cnt = []
        self.start = dict()
        self.end = dict()
        self.idx = dict()
        self.key = dict()

    def _swap(self, k1, k2):
        i, j = self.idx[k1], self.idx[k2]
        self.idx[k1], self.idx[k2] = self.idx[k2], self.idx[k1]
        self.key[i], self.key[j] = self.key[j], self.key[i]

    def _del_empty_range(self, cnt):
        if self.start[cnt] > self.end[cnt]:
            del self.start[cnt]
            del self.end[cnt]

    def inc(self, key: str) -> None:
        if key in self.idx:
            old_idx = self.idx[key]
            old_cnt = self.cnt[old_idx]
            start_key = self.key[self.start[old_cnt]]
            self._swap(key, start_key)
            new_idx = self.idx[key]
            self.cnt[new_idx] += 1
            new_cnt = self.cnt[new_idx]
            self.end[new_cnt] = new_idx
            if new_cnt not in self.start:
                self.start[new_cnt] = new_idx
            self.start[old_cnt] = new_idx + 1
            self._del_empty_range(old_cnt)
        else:
            self.cnt.append(1)
            i = len(self.cnt) - 1
            self.idx[key] = i
            self.key[i] = key
            if 1 in self.end:
                self.end[1] = i
            else:
                self.start[1] = i
                self.end[1] = i

    def dec(self, key: str) -> None:
        if key in self.idx:
            old_idx = self.idx[key]
            old_cnt = self.cnt[old_idx]
            end_key = self.key[self.end[old_cnt]]
            self._swap(key, end_key)
            new_idx = self.idx[key]
            self.cnt[new_idx] -= 1
            new_cnt = self.cnt[new_idx]
            if new_cnt == 0:
                del self.idx[key]
                del self.key[new_idx]
                self.cnt.pop()
            else:
                self.start[new_cnt] = new_idx
                if new_cnt not in self.end:
                    self.end[new_cnt] = new_idx
            self.end[old_cnt] = new_idx - 1
            self._del_empty_range(old_cnt)

    def getMaxKey(self) -> str:
        return self.key[0] if self.cnt else ''

    def getMinKey(self) -> str:
        return self.key[len(self.cnt) - 1] if self.cnt else ''
