class RevTrie:
    def __init__(self):
        self.child = defaultdict(RevTrie)
        self.bow = False

    def _add(self, i, word):
        if i >= 0:
            c = word[i]
            self.child[c]._add(i - 1, word)
            self.child[c].bow = self.child[c].bow or (i == 0)

    def add(self, word):
        self._add(len(word) - 1, word)

    def _search(self, i, word):
        if i < 0:
            return self.bow
        elif self.bow:
            return True
        else:
            c = word[i]
            if c in self.child:
                return self.child[c]._search(i - 1, word)
            else:
                return False

    def search(self, word):
        return self._search(len(word) - 1, word)


class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = RevTrie()
        for w in words:
            self.trie.add(w)
        self.histq = ''

    def query(self, letter: str) -> bool:
        self.histq += letter
        return self.trie.search(self.histq)
