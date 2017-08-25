class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        pairs = []
        for i in xrange(min(k, len(nums1))):
            for j in xrange(min(k, len(nums2))):
                pairs.append((nums1[i], nums2[j]))
        pairs.sort(key=sum)
        return pairs[:k]

