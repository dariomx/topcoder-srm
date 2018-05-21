from bisect import bisect_left


class Trie:
    def __init__(self):
        self.child = dict()
        self.rate = 0
        self.idx = -1

    def add(self, word, rate, idx):
        if len(word) == 0:
            self.rate += rate
            self.idx = idx
        else:
            c = word[0]
            if c not in self.child:
                self.child[c] = Trie()
            self.child[c].add(word[1:], rate, idx)

    def search(self, word):
        if len(word) == 0:
            return self
        else:
            c = word[0]
            if c in self.child:
                return self.child[c].search(word[1:])
            else:
                return None


class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.sentences = dict(((s, i) for (i, s) in enumerate(sentences)))
        self.trie = Trie()
        for s, i in self.sentences.items():
            self.trie.add(s, times[i], i)
        self.root = self.trie
        self.key = ""
        self.ans_len = 3

    def input(self, c):
        if c == "#":
            if self.key not in self.sentences:
                self.sentences[self.key] = len(self.sentences) - 1
            self.trie.add(self.key, 1, self.sentences[self.key])
            self.root = self.trie
            self.key = ""
            return []
        self.key += c
        if not self.root or c not in self.root.child:
            self.root = None
            return []
        self.root = self.root.child[c]
        stack = [(self.root, self.key)]
        ans = []
        while stack:
            node, sent = stack.pop()
            if node.idx >= 0:
                entry = (-node.rate, sent)
                pos = bisect_left(ans, entry)
                ans.insert(pos, entry)
                if len(ans) > self.ans_len:
                    ans.pop()
            for k in node.child:
                stack.append((node.child[k], sent + k))
        return [t[1] for t in ans]
