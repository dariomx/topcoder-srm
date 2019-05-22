class Trie:
    def __init__(self):
        self.child = dict()
        self.eow = False

    def add(self, s):
        if s:
            c = s[0]
            if c not in self.child:
                self.child[c] = Trie()
            self.child[c].add(s[1:])
        else:
            self.eow = True

    def lcp(self, pfx=""):
        n = len(self.child)
        if n == 0 or n > 1 or self.eow:
            return pfx
        else:
            c = next(iter(self.child.keys()))
            return self.child[c].lcp(pfx + c)


class Solution:
    def longestCommonPrefix(self, strs):
        trie = Trie()
        for s in strs:
            trie.add(s)
        return trie.lcp()
