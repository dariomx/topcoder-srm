# lame, a single pass was enough

class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        def clone(node):
            nonlocal nodeMap
            if node is None:
                return None
            else:
                newNode = NodeCopy(node.val, clone(node.left), clone(node.right))
                nodeMap[node] = newNode
                return newNode
        def setRandom(node, orig):
            nonlocal nodeMap
            if node:
                node.random = nodeMap[orig.random]
                setRandom(node.left, orig.left)
                setRandom(node.right, orig.right)
        # main
        nodeMap = {None: None}
        cloned = clone(root)
        setRandom(nodeMap[root], root)
        return cloned