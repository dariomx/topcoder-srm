class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        else:
            return Node(root.val, [self.cloneTree(c) for c in root.children])