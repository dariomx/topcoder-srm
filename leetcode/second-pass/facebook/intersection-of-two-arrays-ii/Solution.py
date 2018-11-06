from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        ans = []
        for x in (cnt1 & cnt2):
            ans += [x] * min(cnt1[x], cnt2[x])
        return ans