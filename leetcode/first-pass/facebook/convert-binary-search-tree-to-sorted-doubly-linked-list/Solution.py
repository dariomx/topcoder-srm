class Solution:
    def inorder(self, root):
        if root:
            yield from self.inorder(root.left)
            yield root
            yield from self.inorder(root.right)

    def treeToDoublyList(self, root):
        head = None
        prev = None
        for node in self.inorder(root):
            if not head:
                head = node
            if prev:
                prev.right = node
                node.left = prev
            prev = node
        if prev:
            prev.right = head
            head.left = prev
        return head