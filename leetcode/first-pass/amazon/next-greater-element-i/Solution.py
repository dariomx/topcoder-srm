class Solution:
    def nextGreaterElement(self, nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        inv2 = dict()
        for i, x in enumerate(nums2):
            inv2[x] = i
        for i in range(n1):
            x = nums1[i]
            nums1[i] = -1
            for j in range(inv2[x]+1, n2):
                if nums2[j] > x:
                    nums1[i] = nums2[j]
                    break
        return nums1