class Trie:
    def __init__(self):
        self.child = dict()
        self.weight = -1

    def add(self, word, weight):
        if len(word) == 0:
            self.weight = weight
        else:
            c = word[0]
            if c not in self.child:
                self.child[c] = Trie()
            self.child[c].add(word[1:], weight)

    def search(self, word):
        if len(word) == 0:
            return self
        else:
            c = word[0]
            if c in self.child:
                return self.child[c].search(word[1:])
            else:
                return None


class WordFilter:
    def __init__(self, words):
        self.words = words
        self.trie = Trie()
        for i in range(len(words)):
            self.trie.add(words[i], i)

    def f(self, prefix, suffix):
        root = self.trie.search(prefix)
        if not root:
            return -1
        k = len(suffix)
        max_weight = -1
        stack = [root]
        while stack:
            node = stack.pop()
            if node.weight > max_weight:
                if k == 0 or self.words[node.weight][-k:] == suffix:
                    max_weight = node.weight
            for c in node.child:
                stack.append(node.child[c])
        return max_weight
