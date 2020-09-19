class Trie:
    def __init__(self):
        self.child = dict()
        self.eow = False

    def setEow(self, s, i):
        self.eow = self.eow or (i == len(s) - 1)

    def add(self, s, i):
        if i < len(s):
            c = s[i]
            if c not in self.child:
                self.child[c] = Trie()
            self.child[c].setEow(s, i)
            self.child[c].add(s, i + 1)

    def search(self, s, j):
        if self.eow:
            yield j - 1
        if j < len(s):
            c = s[j]
            if c in self.child:
                yield from self.child[c].search(s, j + 1)


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        trie = Trie()
        for w in words:
            trie.add(w, 0)
        ans = []
        for i in range(len(text)):
            for j in trie.search(text, i):
                ans.append((i, j))
        return ans
