class Node:
    def __init__(self, val, eow):
        self.val = val
        self.eow = eow
        self.children = dict()

class Solution(object):
    def getVal(self, n):
        return n.val

    def addToTrie(self, word, root):
        n = len(word)
        node = root
        for i in xrange(n):
            c = word[i]
            if c not in node.children:
                node.children[c] = Node(c, i==(n-1))
            node = node.children[c]

    def buildTrie(self, words):
        root = Node(None, False)
        for word in words:
            self.addToTrie(word, root)
        return root

    def findRows(self, k, roots):
        stack = [(roots[0], 0, [])]
        while stack:
            node, d, path = stack.pop()
            if d == k and node.eow:
                yield path + [node]
            else:
                children = node.children.viewkeys()
                if roots[d]:
                    children &= roots[d].children.viewkeys()
                for c in children:
                    child = node.children[c]
                    if d > 0:
                        newPath = path + [node]
                    else:
                        newPath = path
                    stack.append((child, d+1, newPath))

    def combine(self, row, sq):
        yield row
        if len(row) > 1:
            i = 1
            for r in sq:
                yield [row[i]] + r
                i += 1

    def sqWords(self, k, roots):
        if k == 0:
            yield [[]]
        else:
            for row in self.findRows(k, roots):
                try:
                    subRoots = []
                    for i in xrange(1, len(row)):
                        subRoots.append(roots[i].children[row[i].val])
                except KeyError:
                    continue
                for sq in self.sqWords(k-1, subRoots):
                    yield self.combine(row, sq)

    def fmtResults(self, sqs):
        fmtRow = lambda row: "".join(map(self.getVal, row))
        fmtSq = lambda sq: map(fmtRow, sq)
        return map(fmtSq, sqs)

    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        root = self.buildTrie(words)
        k = len(words[0])
        roots = [root] * k
        return self.fmtResults(self.sqWords(k, roots))

words = ["area","lead","wall","lady","ball"]
print(Solution().wordSquares(words))