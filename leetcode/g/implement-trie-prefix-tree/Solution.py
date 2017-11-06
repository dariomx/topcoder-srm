class TrieNode:
    def __init__(self):
        self.child = dict()
        self.eow = False


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        n = len(word)
        for i in xrange(n):
            c = word[i]
            if c not in node.child:
                node.child[c] = TrieNode()
            node = node.child[c]
            node.eow = node.eow or (i == n - 1)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            if c not in node.child:
                return False
            node = node.child[c]
        return node.eow

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            if c not in node.child:
                return False
            node = node.child[c]
        return True



        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)