class TrieNode:
    def __init__(self):
        self.child = dict()
        self.is_word = False

    def __str__(self):
        return str(self.is_word) + ":" + str(self.child)


class WordDictionary(object):
    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word):
        n = len(word)
        node = self.trie
        for i in range(n):
            c = word[i]
            if c not in node.child:
                node.child[c] = TrieNode()
            node = node.child[c]
            node.is_word = node.is_word or ((i + 1) == n)

    def search(self, word):
        n = len(word)
        stack = [(0, self.trie)]
        while stack:
            i, node = stack.pop()
            if i == n:
                if node.is_word:
                    return True
                else:
                    continue
            c = word[i]
            if c == '.':
                for k in node.child:
                    stack.append((i + 1, node.child[k]))
            elif c in node.child:
                stack.append((i + 1, node.child[c]))
        return False
