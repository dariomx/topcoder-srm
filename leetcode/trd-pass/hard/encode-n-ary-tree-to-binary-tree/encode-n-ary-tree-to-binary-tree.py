class Codec:
    def _encodeRight(self, root):
        if root is None:
            return None
        else:
            encRoot = TreeNode(root.val)
            node = encRoot
            for child in root.children:
                node.right = self._encodeLeft(child)
                node = node.right
            return encRoot

    def _encodeLeft(self, root):
        if root is None:
            return None
        else:
            encRoot = TreeNode(root.val)
            node = encRoot
            for child in root.children:
                node.left = self._encodeRight(child)
                node = node.left
            return encRoot

    def _decodeRight(self, root):
        if root is None:
            return None
        else:
            node = Node(root.val, [])
            child = root.right
            while child:
                node.children.append(self._decodeLeft(child))
                child = child.right
            return node

    def _decodeLeft(self, root):
        if root is None:
            return None
        else:
            node = Node(root.val, [])
            child = root.left
            while child:
                node.children.append(self._decodeRight(child))
                child = child.left
            return node

    def encode(self, root: 'Node') -> TreeNode:
        return self._encodeRight(root)

    def decode(self, data: TreeNode) -> 'Node':
        return self._decodeRight(data)
