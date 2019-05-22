class Solution:
    def neighbors(self, word):
        if word in self.neicache:
            return self.neicache[word]
        nei = []
        for i in range(len(word)):
            prefix = word[:i]
            suffix = word[i + 1:]
            for c in "abcdefghijklmnopqrstuvwxyz":
                w = prefix + c + suffix
                if w != word and w in self.words:
                    nei.append(w)
        self.neicache[word] = nei
        return nei

    def dfs(self, node, visited):
        word, path = node
        if self.ans and len(path) > len(self.ans[-1]):
            None
        elif word == self.endWord:
            if not self.ans or len(path) == len(self.ans[-1]):
                self.ans.append(path)
            elif len(path) < len(self.ans[-1]):
                self.ans = [path]
        else:
            for w in self.neighbors(word):
                if w in visited:
                    continue
                visited.add(w)
                self.dfs((w, path + [w]), visited)
                visited.remove(w)

    def findLadders(self, beginWord, endWord, wordList):
        if len(beginWord) == 1:
            return [[beginWord, endWord]]
        self.words = set(wordList)
        self.endWord = endWord
        self.neicache = dict()
        self.ans = []
        self.dfs((beginWord, [beginWord]), set([beginWord]))
        return self.ans
