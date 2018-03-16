class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return "(%d,%d)" % (self.start, self.end)

class Solution:
    def bin_search(self, ivs, niv, ival):
        n = len(ivs)
        start, end = 0, n - 1
        while True:
            mid = (start + end) // 2
            if ival(niv) < ivs[mid].start:
                end = mid - 1
                if start > end:
                    mid = end + 1
                    break
            elif ival(niv) > ivs[mid].end:
                start = mid + 1
                if start > end:
                    mid = start
                    break
            elif ivs[mid].start <= ival(niv) <= ivs[mid].end:
                return mid, True
        return mid, False

    def merge(self, iv1, iv2):
        start = min(iv1.start, iv2.start)
        end = max(iv1.end, iv2.end)
        return Interval(start, end)

    def insert(self, ivs, niv):
        if not ivs:
            return [niv]
        if not niv:
            return ivs
        i, lmerge = self.bin_search(ivs, niv, lambda i: i.start)
        j, rmerge = self.bin_search(ivs, niv, lambda i: i.end)
        print((i, lmerge), (j, rmerge))
        if not lmerge and not rmerge:
            return ivs[:i] + [niv] + ivs[j:]
        else:
            if lmerge:
                middle = self.merge(niv, ivs[i])
            else:
                middle = niv
            if rmerge:
                middle = self.merge(middle, ivs[j])
                j += 1
            return ivs[:i] + [middle] + ivs[j:]


#ivs = [Interval(1,3), Interval(4,5), Interval(6,9)]
#niv = Interval(5.5, 5.6)
ivs = [Interval(iv[0],iv[1]) for iv in ([1,2],[3,5],[6,7],[8,10],[12,16])]
niv = Interval(5,8)
ivs = [Interval(1,3), Interval(6,9)]
niv = Interval(2, 5)
ivs = [Interval(1,5)]
niv = Interval(0, 3)
ivs = [Interval(1,5)]
niv = Interval(0, 6)

soln = Solution()
print([str(iv) for iv in soln.insert(ivs, niv)])