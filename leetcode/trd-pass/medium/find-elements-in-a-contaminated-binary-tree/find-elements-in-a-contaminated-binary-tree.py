class FindElements:
    def __init__(self, root: TreeNode):
        self.values = set()
        def rec(node, val):
            if node:
                self.values.add(val)
                rec(node.left, 2*val + 1)
                rec(node.right, 2*val + 2)
        rec(root, 0)

    def find(self, target: int) -> bool:
        return target in self.values
