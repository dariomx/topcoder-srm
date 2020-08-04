# could not make it, but got adapted this version from other idea
# i saw oh phorum

from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        start = 0
        ans = 0
        cnt = defaultdict(lambda: 0)
        for end in range(len(s)):
            cnt[s[end]] += 1
            while start <= end and len(cnt) > k:
                c = s[start]
                cnt[c] -= 1
                if cnt[c] == 0:
                    del cnt[c]
                start += 1
            ans = max(ans, end - start + 1)
        return ans