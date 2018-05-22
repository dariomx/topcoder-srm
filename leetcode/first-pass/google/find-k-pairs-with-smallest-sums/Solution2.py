class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        pairs = []
        for x in nums1[:k]:
            for y in nums2[:k]:
                pairs.append((x, y))
        pairs.sort(key=sum)
        return pairs[:k]
