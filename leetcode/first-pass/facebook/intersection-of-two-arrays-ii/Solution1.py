class Solution:
    def intersect(self, nums1, nums2):
        i, j = 0, 0
        n, m = len(nums1), len(nums2)
        nums1.sort()
        nums2.sort()
        ans = []
        while i < n and j < m:
            x, y = nums1[i], nums2[j]
            if x == y:
                ans.append(x)
                i += 1
                j += 1
            elif x < y:
                i += 1
            else:
                j += 1
        return ans