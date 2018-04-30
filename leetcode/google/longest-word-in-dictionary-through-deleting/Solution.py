class Solution:
    def is_contained(self, w, s):
        i = 0
        for c in w:
            j = s.find(c, i)
            if j < 0:
                return False
            i = j + 1
        return True

    def findLongestWord(self, s, d):
        max_word = ""
        for w in d:
            if self.is_contained(w, s):
                if len(w) > len(max_word):
                    max_word = w
                elif len(w) == len(max_word) and w < max_word:
                    max_word = w
        return max_word


