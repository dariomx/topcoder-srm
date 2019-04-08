# deliberately adapted from Cormen's book; this one is hard to rememba

class Solution:
    def searchNode(self, root, key, parent):
        if root is None:
            return None, parent
        elif root.val == key:
            return root, parent
        elif key < root.val:
            return self.searchNode(root.left, key, root)
        else:
            return self.searchNode(root.right, key, root)

    # transplant method in Cormen
    def transp(self, root, parent, u, v):
        if parent is None:
            root = v
        elif parent.left == u:
            parent.left = v
        else:
            parent.right = v
        return root

    def findMin(self, root, parent):
        if root is None:
            return None, parent
        node = root
        while node.left:
            parent = node
            node = node.left
        return node, parent

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        node, parent = self.searchNode(root, key, None)
        if node is None:
            return root
        succ, parSucc = self.findMin(node.right, node)
        if node.left is None and node.right is None:
            root = self.transp(root, parent, node, None)
        elif node.left is None and node.right is not None:
            root = self.transp(root, parent, node, node.right)
        elif node.left is not None and node.right is None:
            root = self.transp(root, parent, node, node.left)
        elif succ == node.right:
            succ.left = node.left
            root = self.transp(root, parent, node, succ)
        else:
            root = self.transp(root, parSucc, succ, succ.right)
            succ.right = node.right
            root = self.transp(root, parent, node, succ)
            succ.left = node.left
        return root
