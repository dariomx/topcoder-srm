class Node:
    def __init__(self):
        self.eow = False
        self.child = dict()

    def setEow(self, eow):
        self.eow = self.eow or eow;

class MessageMess:
    AMB = "AMBIGUOUS!"
    IMP = "IMPOSSIBLE!"

    def addToTrie(self, word, root):
        n = len(word)
        node = root
        for i in xrange(n):
            c = word[i]
            if c not in node.child:
                node.child[c] = Node()
            node = node.child[c]
            node.setEow(i==(n-1))

    def buildTrie(self, dictionary):
        root = Node()
        for word in dictionary:
            self.addToTrie(word, root)
        return root

    def searchSoln(self, pfx, cache):
        decMsg = None
        for i in pfx:
            if cache[i] not in [self.AMB, self.IMP]:
                if decMsg is None:
                    decMsg = pfx[i] + cache[i]
                else:
                    return self.AMB
            elif cache[i] == self.AMB:
                return self.AMB
        return self.IMP if decMsg is None else decMsg

    def decRec(self, message, n, i, root, cache):
        if i in cache:
            return cache[i]
        decMsg = ""
        pfx = dict()
        node = root
        for j in xrange(i, n):
            c = message[j]
            if c not in node.child:
                break
            decMsg += c
            node = node.child[c]
            if node.eow:
                if j == (n-1):
                    cache[i] = decMsg
                    pfx[i] = ""
                else:
                    cache[j+1] = self.decRec(message, n, j+1, root, cache)
                    pfx[j+1] = decMsg + " "
        cache[i] = self.searchSoln(pfx, cache)
        return cache[i]

    def restore(self, dictionary, message):
        root = self.buildTrie(dictionary)
        cache = dict()
        return self.decRec(message, len(message), 0, root, cache)

# test
dictionary = ["HI", "YOU", "SAY"]
message = "HIYOUSAYHI"
#dictionary = ["ABC", "BCD", "CD", "ABCB"]
#message = "ABCBCD"
#dictionary = ["IMPOSS", "SIBLE", "S"]
#message = "IMPOSSIBLE"
#dictionary = ["IMPOSS", "SIBLE", "S", "IMPOSSIBLE"]
#message = "IMPOSSIBLE"
#dictionary = ["A", "B", "AB", "BA", "ABA", "BAB", "ABAB", "BABA", "ABABA", "BABAB", "ABABAB", "BABABA", "ABABABA", "BABABAB", "ABABABABABABABABABABABAC"]
#message = "ABABABABABABABABABABABACABABABABABABABABABABABAC"
#dictionary = ["A", "BA", "BAB", "AR"]
#message = "ABABABABABABABABABABABABABABABABABABABABABABABAR"
#message = "A" + "BABA" + "BABAR"
# BAB + A
# BA + BA
print(MessageMess().restore(dictionary, message))