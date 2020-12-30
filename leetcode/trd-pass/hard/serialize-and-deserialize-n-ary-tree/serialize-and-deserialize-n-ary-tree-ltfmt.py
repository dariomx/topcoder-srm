class Codec:
    def serialize(self, root: 'Node') -> str:
        def serialNode(node):
            if node is None:
                return 'null'
            else:
                return '%d' % node.val

        queue = deque([root])
        nodes = [root, None]
        while queue:
            node = queue.popleft()
            if node is None:
                continue
            for child in node.children:
                if child:
                    queue.append(child)
                    nodes.append(child)
            if queue:
                nodes.append(None)
        return ','.join(map(serialNode, nodes))

    def deserialize(self, data: str) -> 'Node':
        def parseNode(s):
            if s == 'null':
                return None
            else:
                return Node(int(s), [])

        nodes = deque((parseNode(s) for s in data.split(',')))
        root = nodes.popleft()
        pend = deque([root])
        cur = None
        while nodes:
            node = nodes.popleft()
            if node is None:
                cur = pend.popleft()
            else:
                cur.children.append(node)
                pend.append(node)
        return root
