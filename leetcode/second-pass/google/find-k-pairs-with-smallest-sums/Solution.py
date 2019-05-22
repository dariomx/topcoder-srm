class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        left, right = [], []
        n, m = len(nums1), len(nums2)
        i, j = 0, 0
        while i < n or j < m:
            if i < n and j < m:
                if nums1[i] == nums2[j]:
                    left.append(nums1[i])
                    right.append(nums2[j])
                    i += 1
                    j += 1
                elif nums1[i] < nums2[j]:
                    left.append(nums1[i])
                    i += 1
                else:
                    right.append(nums2[j])
                    j += 1
            elif i < n:
                left.append(nums1[i])
                i += 1
            else:
                right.append(nums2[j])
                j += 1
            if len(left) * len(right) >= k:
                break
        pairs = []
        for x in left:
            for y in right:
                pairs.append((x, y))
                if len(pairs) == k:
                    return pairs
        return pairs
