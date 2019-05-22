class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def get_depth():
            node = root
            depth = 0
            while node:
                node = node.left
                depth += 1
            return depth

        def conndep(node, cur_dep, tgt_dep):
            nonlocal prev
            if not node:
                return
            if cur_dep == tgt_dep:
                if prev:
                    prev.next = node
                prev = node
            else:
                conndep(node.left, cur_dep + 1, tgt_dep)
                conndep(node.right, cur_dep + 1, tgt_dep)

        # main
        depth = get_depth()
        for d in range(depth + 1):
            prev = None
            conndep(root, 0, d)
        return root

