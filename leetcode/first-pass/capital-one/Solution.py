class Solution:
    def check(self, x, y, x2y):
        if x in x2y:
            if y != x2y[x]:
                return False
        else:
            x2y[x] = y
        return True

    def wordPattern(self, pattern, str):
        words = str.split()
        if len(pattern) != len(words):
            return False
        c2w = dict()
        w2c = dict()
        for c, w in zip(pattern, words):
            if not self.check(c, w, c2w):
                return False
            if not self.check(w, c, w2c):
                return False
        return True
