class Trie:
    def __init__(self):
        self.child = dict()
        self.cnt = 0

    def add(self, i, s):
        c = s[i]
        if c not in self.child:
            self.child[c] = Trie()
        self.child[c].cnt += 1
        if i < len(s) - 1:
            self.child[c].add(i + 1, s)

    def search(self, i, s):
        c = s[i]
        if c not in self.child:
            return False
        elif i == len(s) - 1:
            return self.child[c].cnt > 1
        else:
            return self.child[c].search(i + 1, s)


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            for i in range(len(w)):
                trie.add(0, w[i:])
        ans = []
        for w in words:
            if trie.search(0, w):
                ans.append(w)
        return ans