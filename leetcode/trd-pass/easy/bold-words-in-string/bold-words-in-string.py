from typing import List

from math import inf

class Trie:
    def __init__(self):
        self.child = dict()
        self.eow = False

    def add(self, s):
        if len(s) == 0:
            self.eow = True
        else:
            c = s[0]
            if c not in self.child:
                self.child[c] = Trie()
            self.child[c].add(s[1:])

    def _search(self, s, dep, eow):
        eow = eow or self.eow
        if len(s) == 0 or s[0] not in self.child:
            if eow:
                return dep
            else:
                return 0
        return self.child[s[0]]._search(s[1:], dep + 1, eow)

    def search(self, s):
        return self._search(s, 0, False)


class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        trie = Trie()
        for w in words:
            trie.add(w)
        start = None
        max_end = -inf
        i = 0
        ans = ''
        while i < len(S):
            size = trie.search(S[i:])
            if size <= 0:
                c = S[i]
                if start is not None:
                    ans += S[start:(max_end + 1)] + '</b>'
                    if i > max_end:
                        ans += c
                    i = max(i, max_end) + 1
                else:
                    ans += c
                    i += 1
                start = None
                max_end = -inf
            elif start is None:
                ans += '<b>'
                start = i
                max_end = i + size - 1
                i += 1
            else:
                max_end = max(max_end, i + size - 1)
                i += 1
        if start is not None:
            ans += S[start:(max_end + 1)] + '</b>'
        return ans.replace('</b><b>', '')

# main
soln = Solution()
words = ["e","cab","de","cc","db"]
S = "cbccceeead"
print(soln.boldWords(words, S))
