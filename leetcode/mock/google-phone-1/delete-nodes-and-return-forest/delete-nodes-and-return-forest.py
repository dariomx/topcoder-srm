class Solution:
    def _new_roots(self, node, parent, roots, to_del):
        discarded = False
        if node is None:
            return
        elif node.val in to_del:
            roots.discard(node)
            discarded = True
            if parent is None:
                pass
            elif node == parent.left:
                parent.left = None
            else:
                parent.right = None
        for child in (node.left, node.right):
            if child:
                if discarded:
                    roots.add(child)
                    if child == node.left:
                        node.left = None
                    else:
                        node.right = None
                self._new_roots(child, node, roots, to_del)

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        roots = set([root])
        self._new_roots(root, None, roots, to_delete)
        return roots