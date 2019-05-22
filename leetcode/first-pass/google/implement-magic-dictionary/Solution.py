class Trie:
    def __init__(self):
        self.child = dict()
        self.eow = False

    def add(self, word, i):
        if i < len(word):
            c = word[i]
            if c not in self.child:
                self.child[c] = Trie()
            self.child[c].eow = self.child[c].eow or \
                                (i == len(word) - 1)
            self.child[c].add(word, i + 1)

    def search(self, word, i, modif):
        if i == len(word):
            return self.eow and modif == 1
        c = word[i]
        if modif <= 1:
            for k in self.child:
                if self.child[k].search(word, i + 1,
                                        modif + int(c != k)):
                    return True
        return False


class MagicDictionary:
    def __init__(self):
        self.trie = Trie()

    def buildDict(self, dict: List[str]) -> None:
        for word in dict:
            self.trie.add(word, 0)

    def search(self, word: str) -> bool:
        return self.trie.search(word, 0, 0)
