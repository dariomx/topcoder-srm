class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def insert(r, val):
    def ins(node):
        ret = node
        if not node:
            ret = Node(val)
        elif val < node.data:
            node.left = ins(node.left)
        elif val > node.data:
            node.right = ins(node.right)
        return ret
    return ins(r)

res = insert(None, 6)
print(res)