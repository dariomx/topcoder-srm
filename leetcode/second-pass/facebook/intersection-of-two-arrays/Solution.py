# O(n log(n) + m log(m)) time Python3 solution without using set/dict

class Solution:
    def intersection(self, nums1, nums2):
        i, n = 0, len(nums1)
        j, m = 0, len(nums2)
        nums1.sort()
        nums2.sort()
        ans = []
        while i < n and j < m:
            x, y = nums1[i], nums2[j]
            if x == y:
                if not ans or ans[-1] != x:
                    ans.append(x)
                i += 1
                j += 1
            elif x < y:
                i += 1
            else:
                j += 1
        return ans