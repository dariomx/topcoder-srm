class Solution(object):
    def comb(self, n, i, k, curr):
        if len(curr) == k:
            yield list(curr)
        elif i < n:
            for c in self.comb(n, i + 1, k, curr):
                yield c
            curr.add(i)
            for c in self.comb(n, i + 1, k, curr):
                yield c
            curr.remove(i)

    def getComb(self, n, k):
        return self.comb(n, 0, k, set())

    def getRanges(self, idxs):
        ranges = []
        idxs.sort()
        start, end = idxs[0], idxs[0]
        for i in xrange(1, len(idxs)):
            if idxs[i] - idxs[i - 1] > 1:
                ranges.append((start, end))
                start, end = idxs[i], idxs[i]
            else:
                end = idxs[i]
        ranges.append((start, end))
        return ranges

    def getAbbrs(self, s):
        n = len(s)
        yield s, n
        for k in xrange(1, n + 1):
            for comb in self.getComb(n, k):
                ranges = self.getRanges(comb)
                abbr, lenAbbr = '', 0
                last = -1
                for i, j in ranges:
                    chunk = s[last + 1:i]
                    abbr += chunk + str(j - i + 1)
                    lenAbbr += len(chunk) + 1
                    last = j
                chunk = s[ranges[-1][1] + 1:]
                abbr += chunk
                lenAbbr += len(chunk)
                yield abbr, lenAbbr

    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        abbrs = set()
        for w in dictionary:
            for a, _ in self.getAbbrs(w):
                abbrs.add(a)
        minAbbr, minLen = '', len(target) + 1
        for a, la in self.getAbbrs(target):
            if a not in abbrs and la < minLen:
                minAbbr = a
                minLen = la
        return minAbbr


target = "apple"
dictionary = ["blade"]
print(Solution().minAbbreviation(target, dictionary))
