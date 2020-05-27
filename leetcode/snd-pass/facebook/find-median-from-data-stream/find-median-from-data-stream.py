from sortedcontainers import SortedList


# Provides indexing about an stream of data, leveraging the fact that most of
# the data will fall into a known range [minVal, maxVal]. Inspired in t-digest.
class DistList:
    def __init__(self, minVal, maxVal):
        self.minVal, self.maxVal = minVal, maxVal
        self.leftTail = SortedList()
        self.hist = [0] * (maxVal - minVal + 1)
        self.histSize = 0
        self.rightTail = SortedList()

    def add(self, val):
        if val < self.minVal:
            self.leftTail.add(val)
        elif self.minVal <= val <= self.maxVal:
            self.hist[val] += 1
            self.histSize += 1
        else:
            self.rightTail.add(val)

    def __len__(self):
        return len(self.leftTail) + self.histSize + len(self.rightTail)

    def __getitem__(self, index):
        leftOffset = len(self.leftTail)
        middleOffset = leftOffset + self.histSize
        rightOffset = middleOffset + len(self.rightTail)
        if index < leftOffset:
            val = self.leftTail[index]
        elif leftOffset <= index < middleOffset:
            val = self._get_from_hist(index - leftOffset)
        elif index < rightOffset:
            val = self.rightTail[index - middleOffset]
        else:
            raise ValueError('Invalid index: %s' % str(index))
        return val

    def _get_from_hist(self, index):
        offset = -1
        val = self.minVal
        while offset + self.hist[val] < index:
            offset += self.hist[val]
            val += 1
        return val


class MedianFinder:
    def __init__(self):
        self.distList = DistList(0, 100)

    def addNum(self, num: int) -> None:
        self.distList.add(num)

    def findMedian(self) -> float:
        size = len(self.distList)
        if size == 0:
            return None
        half = size // 2
        if size % 2 == 0:
            median = (self.distList[half - 1] + self.distList[half]) / 2
        else:
            median = self.distList[half]
        return median
