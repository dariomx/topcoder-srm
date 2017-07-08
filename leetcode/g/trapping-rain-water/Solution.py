class Solution(object):
    def countLevel(self, level, height):
        totalCnt = 0
        cnt = 0
        valley = False
        for i in xrange(1, len(height)):
            if height[i] < level:
                if not valley and height[i - 1] >= level:
                    valley = True
                if valley:
                    cnt += 1
            elif valley:
                totalCnt += cnt
                valley = False
                cnt = 0
        return totalCnt

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        cnt = 0
        levels = sorted(set(height))
        for i in xrange(1, len(levels)):
            fillFactor = levels[i] - levels[i - 1]
            cnt += fillFactor * self.countLevel(levels[i], height)
        return cnt