class Solution:
    def flatten(self, root: 'TreeNode') -> 'None':
        def rec(node):
            if not node:
                return None, None
            else:
                head, tail = node, node
                for child in (node.left, node.right):
                    h, t = rec(child)
                    tail.right = h
                    tail.left = None
                    if t:
                        tail = t
                return head, tail

        rec(root)
