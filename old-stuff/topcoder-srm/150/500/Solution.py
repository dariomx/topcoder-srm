import sys

class StripePainter:
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

    def initCache(self, stripes):
        cache = dict()
        for i in xrange(len(stripes)):
            cache[(i, i)] = 1
        return cache

    def recMinStrokes(self, stripes, start, end, usedColors, cache):
        n = len(stripes)
        if not(0 <= start < n and 0 <= end < n and start <= end):
            return sys.maxint
        elif (start, end) in cache:
            return cache[(start, end)]
        else:
            minS = sys.maxint
            for color in set(stripes[start:end+1]) - usedColors:
                kMinS = 1
                usedColors.add(color)
                for i, j in self.colorSplit(stripes, start, end, color):
                    kMinS += self.recMinStrokes(stripes, i, j, usedColors, cache)
                minS = min(minS, kMinS)
                usedColors.remove(color)
            cache[(start, end)] = minS
            return minS

    def minStrokes(self, stripes):
        return self.recMinStrokes(stripes, 0, len(stripes)-1, \
                                  set(), self.initCache(stripes))

stripes = "RGBGR"
stripes = "RGRG"
stripes = "ABACADA"
stripes = "AABBCCDDCCBBAABBCCDD"
stripes = "BECBBDDEEBABDCADEAAEABCACBDBEECDEDEACACCBEDABEDADD"
stripes = "ABCDEFGHIJKLMNOPQRSTUVWQWVUTSRQPONMLKJIHGFEDCBA"
stripes = "ABCACBA"
print(StripePainter().minStrokes(stripes))
