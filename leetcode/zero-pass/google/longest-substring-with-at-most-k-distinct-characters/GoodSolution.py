# this does not look like my style, where did i get it?
# ah, from here
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/discuss/80052/10-line-Python-Solution-using-dictionary-with-easy-to-understand-explanation
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        d = {}
        low, ret = 0, 0
        for i, c in enumerate(s):
            d[c] = i
            if len(d) > k:
                low = min(d.values())
                del d[s[low]]
                low += 1
            ret = max(i - low + 1, ret)
        return ret
