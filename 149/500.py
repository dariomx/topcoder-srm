class Node:
    def __init__(self):
        self.eow = False
        self.child = dict()

    def setEow(self, eow):
        self.eow = self.eow or eow;

class MessageMess:
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

    def handleEow(self, j, n, msg, decMsg, pending, failed):
        exit = False
        if j == (n - 1):
            if decMsg is None:
                decMsg = msg.strip()
            else:
                decMsg = "AMBIGUOUS!"
                exit = True
        else:
            if (j+1) not in failed:
                pending.append((msg + " ", j + 1))
        return decMsg, exit

    def updateFailed(self, i, n, failed):
        for j in xrange(i+1, n):
            if j not in failed:
                return
        failed.add(i)

    def restore(self, dictionary, message):
        n = len(message)
        root = self.buildTrie(dictionary)
        pending = [("", 0)]
        failed = set()
        decMsg = None
        exit = False
        while pending:
            if exit:
                break
            msg, i = pending.pop()
            print((msg, i))
            node = root
            for j in xrange(i, n):
                c = message[j]
                if c not in node.child:
                    self.updateFailed(i, n, failed)
                    break
                msg += c
                node = node.child[c]
                if node.eow:
                    decMsg, exit = \
                        self.handleEow(j, n, msg, decMsg, pending, failed)
                if exit:
                    break
        if decMsg is None:
            decMsg = "IMPOSSIBLE!"
        return decMsg

# test
#dictionary = ["HI", "YOU", "SAY"]
#message = "HIYOUSAYHI"
#dictionary = ["ABC", "BCD", "CD", "ABCB"]
#message = "ABCBCD"
#dictionary = ["IMPOSS", "SIBLE", "S"]
#message = "IMPOSSIBLE"
#dictionary = ["IMPOSS", "SIBLE", "S", "IMPOSSIBLE"]
#message = "IMPOSSIBLE"
dictionary = ["A", "B", "AB", "BA", "ABA", "BAB", "ABAB", "BABA", "ABABA", "BABAB", "ABABAB", "BABABA", "ABABABA", "BABABAB", "ABABABABABABABABABABABAC"]
message = "ABABABABABABABABABABABACABABABABABABABABABABABAC"
#dictionary = ["A", "BA", "BAB", "AR"]
#message = "ABABABABABABABABABABABABABABABABABABABABABABABAR"
print(MessageMess().restore(dictionary, message))