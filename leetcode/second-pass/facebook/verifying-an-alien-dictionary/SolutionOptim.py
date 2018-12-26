class Solution:
    def isAlienSorted(self, words, order):
        order = {c:i for (i,c) in enumerate(order)}
        order[' '] = -1
        def lexcmp(w1, w2):
            if len(w1) < len(w2):
                w1 = w1.ljust(len(w2))
            elif len(w2) < len(w1):
                w2 = w2.ljust(len(w1))
            for i in range(len(w1)):
                if order[w1[i]] < order[w2[i]]:
                    return -1
                elif order[w1[i]] > order[w2[i]]:
                    return +1
            return True
        for i in range(len(words)-1):
            if lexcmp(words[i], words[i+1]) > 0:
                return False
        return True