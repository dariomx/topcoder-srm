import sys

class StripePainter:
    def prefix(self, arr, start, tgt):
        i = start
        n = len(tgt)
        while i < n and arr[i] == tgt[i]:
            i += 1
        return i

    def postfix(self, arr, start, tgt):
        i = start
        while i >=0 and arr[i] == tgt[i]:
            i -= 1
        return i

    def colorSplit(self, stripes, start, end, color):
        i, j = None, None
        for k in xrange(start, end+1):
            if stripes[k] == color:
                if i is not None and j is not None:
                    yield i, j
                i, j = None, None
            else:
                if i is None:
                    i = k
                j = k
        if stripes[end] != color and i is not None and j is not None:
            yield i, j

    def fill(self, arr, start, end, x, tgt=None):
        for k in xrange(start, end + 1):
            if tgt is None or tgt[k] == x:
                arr[k] = x

    def initCache(self, stripes):
        cache = dict()
        for i in xrange(len(stripes)):
            cache[(i, i)] = 1
        return cache

    def singletonStrategy(self, arr, i, stripes):
        if arr[i] == stripes[i]:
            return 0
        else:
            arr[i] = stripes[i]
            return 1

    def fillingStrategy(self, arr, start, end, stripes, cache, i, j, color):
        if arr[start:end+1] == arr[i:j+1] and set(arr[start:end+1]) != set([None]):
            return sys.maxint
        else:
            self.fill(arr, i, j, color)
            return 1 + self.recMinStrokes(arr, i, j, stripes, cache)

    def holesStrategy(self, arr, start, end, stripes, cache, i, j, color):
        self.fill(arr, i, j, color, stripes)
        minStrokes = 1
        for x, y in self.colorSplit(stripes, i, j, color):
            minS = self.recMinStrokes(arr, x, y, stripes, cache)
            if minS == sys.maxint:
                return sys.maxint
            else:
                minStrokes += minS
        return minStrokes

    def recMinStrokes(self, arr, start, end, stripes, cache):
        if (start, end) in cache:
            return cache[(start, end)]
        i = self.prefix(arr, start, stripes)
        j = self.postfix(arr, end, stripes)
        if i > j:
            ret = 0
        elif i == j:
            ret = self.singletonStrategy(arr, i, stripes)
        else:
            minStrokes = sys.maxint
            bkpArr = list(arr)
            for color in set(stripes[i:j+1]):
                minStrokes = min(minStrokes,
                                 self.fillingStrategy(arr, start, end, stripes,
                                                      cache, i, j, color))
                arr = list(bkpArr)
                minStrokes = min(minStrokes,
                                 self.holesStrategy(arr, start, end, stripes,
                                                    cache, i, j, color))
            ret = minStrokes
        cache[(start, end)] = ret
        return ret

    def minStrokes(self, stripes):
        n = len(stripes)
        arr = [None] * n
        return self.recMinStrokes(arr, 0, n-1, stripes, self.initCache(stripes))

stripes = "RGBGR"
stripes = "RGRG"
stripes = "ABACADA"
stripes = "AABBCCDDCCBBAABBCCDD"
#stripes = "BECBBDDEEBABDCADEAAEABCACBDBEECDEDEACACCBEDABEDADD"
#stripes = "ABCDEFGHIJKLMNOPQRSTUVWQWVUTSRQPONMLKJIHGFEDCBA"
#stripes = "QRSQSRQ"
#stripes = "ABCDEFGHIJKLMNOPQRSTUVWQQQWVUTSRQPONMLKJIHGFEDCBA"
print(StripePainter().minStrokes(stripes))