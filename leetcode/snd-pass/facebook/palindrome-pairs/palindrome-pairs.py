class Trie:
    def __init__(self):
        self.child = dict()
        self.eow = False
        self.i = -1

    def add(self, word, i):
        if len(word) > 0:
            c = word[0]
            if c not in self.child:
                self.child[c] = Trie()
            self.child[c].add(word[1:], i)
            if len(word) == 1:
                self.child[c].eow = self.child[c].eow or True
                self.child[c].i = i

    def search(self, word):
        if len(word) > 0:
            c = word[0]
            if c in self.child:
                return self.child[c].search(word[1:])
            else:
                return None
        else:
            return self

    def words_from(self):
        if self.eow:
            yield self.i
        for c in self.child:
            yield from self.child[c].words_from()


class Solution:
    def isPalindrome(self, w):
        return w == w[::-1]

    def buildTrie(self, words):
        trie = Trie()
        for i, w in enumerate(words):
            if w == '':
                trie.eow = True
                trie.i = i
            else:
                trie.add(w, i)
        return trie

    def addPairs(self, i, words, node, revWord, ans):
        if node is not None:
            for j in node.words_from():
                if i == j:
                    continue
                if not revWord and self.isPalindrome(words[i] + words[j]):
                    ans.append((i, j))
                elif revWord and self.isPalindrome(words[j] + words[i]):
                    ans.append((j, i))

    def getPairs(self, words, revTrie=False):
        if revTrie:
            wordsTrie = map(lambda w: w[::-1], words)
        else:
            wordsTrie = words
        trie = self.buildTrie(wordsTrie)
        ans = []
        for i, w in enumerate(words):
            if revTrie:
                node = trie.search(w)
                self.addPairs(i, words, node, False, ans)
            else:
                node = trie.search(w[::-1])
                self.addPairs(i, words, node, True, ans)
        return ans

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ansFwd = self.getPairs(words)
        ansRev = self.getPairs(words, revTrie=True)
        return list(set(ansFwd + ansRev))