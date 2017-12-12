from bisect import bisect_left, bisect_right


class Solution(object):
    def search_pos(self, k, arr1, arr2, bisfunc):
        start, end = 0, len(arr1) - 1
        while start <= end:
            mid = (start + end) / 2
            pos = mid + bisfunc(arr2, arr1[mid])
            if pos == k:
                return arr1[mid]
            elif pos < k:
                start = mid + 1
            else:
                end = mid - 1
        return None

    def search_pos_both(self, k, arr1, arr2):
        pos = self.search_pos(k, arr1, arr2, bisect_left)
        if pos is None:
            pos = self.search_pos(k, arr2, arr1, bisect_right)
        return pos

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1) + len(nums2)
        median = float(self.search_pos_both(n / 2, nums1, nums2))
        if n % 2 == 0:
            median += self.search_pos_both(n / 2 - 1, nums1, nums2)
            median /= 2.0
        return median
