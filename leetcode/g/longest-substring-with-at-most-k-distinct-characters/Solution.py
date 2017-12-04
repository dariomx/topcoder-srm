class Solution(object):
    def findLen(self, s, k, start, end, incr, chars):
        chars.clear()
        for i in xrange(start, end + incr, incr):
            if s[i] in chars:
                xLen = 0
            else:
                xLen = 1
            if len(chars) + xLen > k:
                break
            chars.add(s[i])
        return abs(start - i)

    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0
        chars = set(s)
        n = len(s)
        if len(chars) <= k:
            return n
        n = len(s)
        start, end = 0, n - 1
        leftLen, rightLen = 0, 0
        while start < end:
            leftLen = self.findLen(s, k, start, end, 1, chars)
            rightLen = self.findLen(s, k, end, start, -1, chars)
            if (leftLen + rightLen) >= (end - start + 1):
                break
            elif leftLen < rightLen:
                start += leftLen
            else:
                end -= rightLen
        return max(leftLen, rightLen)


print(Solution().lengthOfLongestSubstringKDistinct("aba", 1))
