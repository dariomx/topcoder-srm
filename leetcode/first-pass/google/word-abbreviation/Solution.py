from collections import defaultdict


class Trie:
    def __init__(self):
        self.cnt = 0
        self.child = dict()

    def add(self, word, i=0):
        if i < len(word):
            c = word[i]
            if c not in self.child:
                self.child[c] = Trie()
            self.child[c].cnt += 1
            self.child[c].add(word, i + 1)

    def search_uniq(self, word, i=0):
        if i == len(word) or self.cnt == 1:
            return 0
        else:
            return 1 + self.child[word[i]].search_uniq(word, i + 1)


class Solution:
    def wordsAbbreviation(self, dictio):
        tries = defaultdict(lambda: Trie())
        for word in dictio:
            n = len(word)
            if n > 3:
                tries[n].add(word[-1] + word)
        ans = []
        for word in dictio:
            n = len(word)
            if n > 3:
                k = tries[n].search_uniq(word[-1] + word)
                if k > 1:
                    k -= 1
                abbr = word[:k] + str(n - k - 1) + word[-1]
                if len(abbr) >= n:
                    abbr = word
                ans.append(abbr)
            else:
                ans.append(word)
        return ans
