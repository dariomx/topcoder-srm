class BinTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

def findCommonAnc(node1, node2):
    turn = 1
    while node1 is not None or node1 is not None:
        if node1 == node2:
            return node1
        if turn == 1:
            node1 = node1.parent
            turn = 2
        else:
            node2 = node2.parent
            turn = 1
    return None
