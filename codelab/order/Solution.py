class Solution:
    # @param heights : list of integers
    # @param infronts : list of integers
    # @return a list of integers
    def order(self, heights, infronts):
        n = len(heights)

        #
        def getNextIdx(start, decrLT):
            minFnt = infronts[start]
            minHgt = heights[start]
            minIdx = start
            for i in xrange(start + 1, n):
                if decrLT is not None and heights[i] < decrLT:
                    infronts[i] -= 1
                if (infronts[i], heights[i]) < (minFnt, minHgt):
                    minFnt, minHgt, minIdx = infronts[i], heights[i], i
            return minIdx

        #
        def swap(i, j):
            heights[i], heights[j] = heights[j], heights[i]
            infronts[i], infronts[j] = infronts[j], infronts[i]

        #
        decrLT = None
        for i in xrange(n - 1):
            idx = getNextIdx(i, decrLT)
            swap(i, idx)
            decrLT = heights[i]
        return heights

#main
heights = [7,29, 82, 30, 62, 23, 67, 35]
infronts = [7, 5, 0, 2, 0, 3, 1, 1]
print(Solution().order(heights, infronts))

