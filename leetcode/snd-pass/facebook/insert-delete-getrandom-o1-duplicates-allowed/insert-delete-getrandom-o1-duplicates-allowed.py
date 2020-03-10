from collections import defaultdict
from random import randint


class RandomizedCollection:
    def __init__(self):
        self.vals = defaultdict(set)
        self.arr = []

    def insert(self, x: int) -> bool:
        exists = x in self.vals
        i = len(self.arr)
        self.vals[x].add(i)
        self.arr.append(x)
        return not exists

    def remove(self, x: int) -> bool:
        if x in self.vals:
            i = self.vals[x].pop()
            if len(self.vals[x]) == 0:
                del self.vals[x]
            j = len(self.arr) - 1
            if i != j:
                y = self.arr[j]
                self.vals[y].remove(j)
                self.vals[y].add(i)
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            self.arr.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        i = randint(0, len(self.arr) - 1)
        return self.arr[i]
