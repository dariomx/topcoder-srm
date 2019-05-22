class Solution:
    def countNodes(self, root: 'TreeNode') -> 'int':
        def rec(node, h):
            nonlocal height, nleaves
            if not node.left and not node.right:
                if not height:
                    height = h
                elif h < height:
                    raise ValueError("found last node!")
                nleaves += 1
            elif node.left and not node.right:
                if not height:
                    height = h + 1
                nleaves += 1
                raise ValueError("found last node!")
            else:
                rec(node.left, h + 1)
                rec(node.right, h + 1)

        if root:
            height, nleaves = None, 0
            try:
                rec(root, 0)
            except ValueError:
                None
            return 2 ** height - 1 + nleaves
        else:
            return 0

