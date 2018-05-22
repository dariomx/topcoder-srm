class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        ans = 0
        n = len(citations)
        citations.sort(reverse=True)
        for i in xrange(1, n + 1):
            if citations[i - 1] >= i:
                ans = i
            else:
                break
        return ans
