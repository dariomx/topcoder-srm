class Trie:
    def __init__(self):
        self.child = dict()
        self.is_word = False

    def insert(self, word):
        node = self
        n = len(word)
        for i in range(n):
            c = word[i]
            if c not in node.child:
                node.child[c] = Trie()
            node = node.child[c]
        node.is_word = True

    def int_search(self, word, is_prefix):
        node = self
        for i in range(len(word)):
            c = word[i]
            if c in node.child:
                node = node.child[c]
            else:
                return False
        return True if is_prefix else node.is_word

    def search(self, word):
        return self.int_search(word, False)

    def startsWith(self, prefix):
        return self.int_search(prefix, True)
