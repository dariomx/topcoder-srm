class Node:
    def __init__(self):
        self.child = dict()
        self.is_word = False


class Solution(object):
    def build_trie(self, dic):
        trie = Node()
        for word in dic:
            node = trie
            n = len(word)
            for i in xrange(n):
                c = word[i]
                if c not in node.child:
                    node.child[c] = Node()
                node = node.child[c]
                node.is_word = (i == n - 1)
        return trie

    def get_match(self, trie, word, start):
        node = trie
        ret = (False, start)
        for i in xrange(start, len(word)):
            c = word[i]
            if c in node.child:
                node = node.child[c]
                if node.is_word:
                    ret = (True, i)
            else:
                break
        return ret

    def get_max_match(self, trie, word, start):
        ret = (False, start)
        for i in xrange(start, len(word)):
            match, end = self.get_match(trie, word, i)
            # print("trying %s[%d,%d:] = (%s,%d)" % (word, start, i, match, end))
            if match and end >= ret[1]:
                ret = (True, end)
            else:
                break
        return ret

    def tag_str(self, s, idxs):
        out = ''
        for start, end, tag in idxs:
            subw = s[start:end + 1]
            if tag:
                out += '<b>' + subw + '</b>'
            else:
                out += subw
        return out

    def addBoldTag(self, s, dic):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        if not s or not dic:
            return s
        trie = self.build_trie(dic)
        start, end = 0, 0
        idxs = []
        while end < len(s) - 1:
            match, end = self.get_max_match(trie, s, start)
            if match and idxs:
                lstart, lend, lmatch = idxs[-1]
                if lmatch and lend + 1 == start:
                    idxs.pop()
                    start = lstart
            idxs.append((start, end, match))
            start = end + 1
            # print(idxs)
        return self.tag_str(s, idxs)
