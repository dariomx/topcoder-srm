class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        node = p
        path_p = set()
        while node:
            path_p.add(node)
            node = node.parent
        node = q
        while node not in path_p:
            node = node.parent
        return node