class Trie:
    def __init__(self):
        self.child = dict()

    def add(self, s):
        trie = self
        for c in s:
            if c not in trie.child:
                trie.child[c] = Trie()
            trie = trie.child[c]

    def search(self, s):
        trie = self
        i = 0
        while i < len(s):
            c = s[i]
            if c in trie.child:
                trie = trie.child[c]
                i += 1
            else:
                break
        return i


class Solution(object):
    def gen_pfxs(self, s):
        n = len(s)
        for i in xrange(n - 1, -1, -1):
            yield s[i:]
            yield s[:i + 1]

    def create_pfx_trie(self, s):
        trie = Trie()
        for ss in self.gen_pfxs(s):
            trie.add(ss)
        return trie

    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        trie_A = self.create_pfx_trie(A)
        max_len = 0
        n = len(B)
        for ss in self.gen_pfxs(B):
            if len(ss) >= max_len:
                max_len = max(max_len, trie_A.search(ss))
        return max_len
