from collections import defaultdict

class Solution(object):
    def is_shared(self, word, chars, cnt):
        for c in chars[word]:
            if cnt[c] > 1:
                return True
        return False

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        chars = dict()
        for w in words:
            chars[w] = set(w)
        cnt = defaultdict(lambda: 0)
        for w in words:
            for c in chars[w]:
                cnt[c] += 1
        max1, max2 = 0, 0
        for w in words:
            if not self.is_shared(w, chars, cnt):
                lenw = len(w)
                if lenw > max1:
                    max2 = max1
                    max1 = lenw
                elif lenw > max2:
                    max2 = lenw
        return max1 * max2

words = ["abcw","baz","foo","bar","xtfn","abcdef"]
print(Solution().maxProduct(words))