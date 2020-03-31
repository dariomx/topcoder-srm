# not really used, just for practicing; inputs are already nodes
def build_quad(self, seq):
    seq = deque(seq)
    queue = deque()

    def new_node():
        tup = seq.popleft()
        if tup is None:
            node = None
        else:
            val, isLeaf = tup
            node = Node(val, isLeaf, None, None, None, None)
            queue.append(node)
        return node

    root = new_node()
    while seq:
        node = queue.popleft()
        node.topLeft = new_node()
        node.topRight = new_node()
        node.bottomLeft = new_node()
        node.bottomRight = new_node()
    return root