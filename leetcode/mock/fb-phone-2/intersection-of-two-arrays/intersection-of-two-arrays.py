class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if nums1:
            nums1.sort()
        if nums2:
            nums2.sort()
        i, j = 0, 0
        n, m = len(nums1), len(nums2)
        ans = []
        while i < n and j < m:
            if nums1[i] == nums2[j]:
                if len(ans) == 0 or nums1[i] != ans[-1]:
                    ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return ans