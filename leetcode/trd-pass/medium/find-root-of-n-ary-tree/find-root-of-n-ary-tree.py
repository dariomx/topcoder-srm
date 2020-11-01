class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        children = set()
        for node in tree:
            if node.children is None:
                continue
            children.update(node.children)
        for node in tree:
            if node in children:
                continue
            else:
                return node