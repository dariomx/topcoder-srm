class Codec:
    def serialize(self, root: 'Node') -> str:
        def serialNode(node):
            if node is None:
                return '-1,0'
            else:
                return '%d,%d' % (node.val, len(node.children))

        queue = deque([root])
        nodes = [root]
        while queue:
            node = queue.popleft()
            if node is None:
                continue
            for child in node.children:
                if child:
                    queue.append(child)
                nodes.append(child)
        return ' '.join(map(serialNode, nodes))

    def deserialize(self, data: str) -> 'Node':
        def parseNode(s):
            val, cnt = map(int, s.split(','))
            if val < 0:
                return None
            else:
                return Node(val, [None] * cnt)

        nodes = deque((parseNode(s) for s in data.split(' ')))
        root = nodes.popleft()
        pend = deque([root])
        while pend:
            node = pend.popleft()
            if node is None:
                continue
            for i in range(len(node.children)):
                node.children[i] = nodes.popleft()
                if node.children[i]:
                    pend.append(node.children[i])
        return root
