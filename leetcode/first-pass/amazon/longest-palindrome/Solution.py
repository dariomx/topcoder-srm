from collections import Counter


class Solution:
    def longestPalindrome(self, s):
        ans = 0
        single = 0
        for cnt in Counter(s).values():
            ans += cnt // 2
            if single == 0:
                single = cnt % 2
        return ans * 2 + single
