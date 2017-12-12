from collections import defaultdict


class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.size = 0
        self.values = []
        self.valCnt = defaultdict(lambda: 0)
        self.medIdx1 = None
        self.medIdx2 = None
        self.median = None

    def insert(self, arr, x):
        start, end = 0, len(arr) - 1
        idx = 0
        while start <= end:
            mid = (start + end) / 2
            if x < arr[mid]:
                if mid == 0 or x > arr[mid - 1]:
                    idx = mid
                    break
                else:
                    end = mid - 1
            elif x > arr[mid]:
                if mid == len(arr) - 1 or x < arr[mid + 1]:
                    idx = mid + 1
                    break
                else:
                    start = mid + 1
            else:
                idx = None
                break
        if idx is not None:
            arr.insert(idx, x)
            if idx <= self.medIdx1:
                self.medIdx1 += 1
        self.size += 1

    def updateMedian(self, x):
        self.valCnt[x] += 1
        trans = False
        if self.size == 1:
            self.medIdx1 = 0
            self.medIdx2 = 1
        elif x < self.values[self.medIdx1]:
            self.medIdx2 -= 0.5
            if self.medIdx2 < 1:
                self.medIdx1 -= 1
                self.medIdx2 = self.valCnt[self.values[self.medIdx1]] + 0.5
                trans = True
        else:
            self.medIdx2 += 0.5
            trans = self.medIdx2 > self.valCnt[self.values[self.medIdx1]]
            if int(self.medIdx2) > self.valCnt[self.values[self.medIdx1]]:
                self.medIdx1 += 1
                self.medIdx2 = 1
        if self.size % 2 == 0 and trans:
            self.median = (self.values[self.medIdx1] + self.values[
                self.medIdx1 + 1]) / 2.0
        else:
            self.median = self.values[self.medIdx1]

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        self.insert(self.values, num)
        self.updateMedian(num)

    def findMedian(self):
        """
        :rtype: float
        """
        return float(self.median)


soln = MedianFinder()
soln.addNum(40)
print(soln.findMedian())
soln.addNum(12)
print(soln.findMedian())
soln.addNum(16)
print(soln.findMedian())
