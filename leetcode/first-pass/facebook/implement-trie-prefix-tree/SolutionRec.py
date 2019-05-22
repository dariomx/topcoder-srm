class Trie:
    def __init__(self):
        self.child = dict()
        self.is_word = False

    def insert(self, word):
        if len(word) == 0:
            self.is_word = True
        else:
            c = word[0]
            if c not in self.child:
                self.child[c] = Trie()
            self.child[c].insert(word[1:])

    def int_search(self, word, is_prefix):
        if len(word) == 0:
            return True if is_prefix else self.is_word
        else:
            c = word[0]
            if c in self.child:
                return self.child[c].int_search(word[1:], is_prefix)
            else:
                return False

    def search(self, word):
        return self.int_search(word, False)

    def startsWith(self, prefix):
        return self.int_search(prefix, True)
