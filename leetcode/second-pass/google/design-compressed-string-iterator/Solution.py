from collections import deque


class StringIterator:
    def __init__(self, compressedString):
        self.cnt = deque()
        i = 0
        k = len(compressedString)
        while i < k:
            c = compressedString[i]
            i += 1
            n = ""
            while i < k and compressedString[i].isdigit():
                n += compressedString[i]
                i += 1
            n = int(n)
            self.cnt.append([c, n])

    def next(self):
        if self.cnt:
            ret = self.cnt[0][0]
            self.cnt[0][1] -= 1
            if self.cnt[0][1] == 0:
                self.cnt.popleft()
            return ret
        else:
            return " "

    def hasNext(self):
        return len(self.cnt) > 0
