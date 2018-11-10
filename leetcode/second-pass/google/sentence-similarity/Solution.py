class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False
        sim = set()
        for x, y in pairs:
            sim.add((x, y))
            sim.add((y, x))
        for x, y in zip(words1, words2):
            if x != y and (x, y) not in sim and (y, x) not in sim:
                return False
        return True

