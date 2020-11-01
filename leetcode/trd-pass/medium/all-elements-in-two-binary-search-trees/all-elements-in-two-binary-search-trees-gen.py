# not sure why using generators is so slow ... exceptions or generators
# themselves are guilty?
class Solution:
    def inorder(self, root):
        if root:
            yield from self.inorder(root.left)
            yield root
            yield from self.inorder(root.right)

    def safeNext(self, gen):
        try:
            return next(gen)
        except StopIteration:
            return None

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        gen1, gen2 = self.inorder(root1), self.inorder(root2)
        node1, node2 = self.safeNext(gen1), self.safeNext(gen2)
        ans = []
        while node1 or node2:
            if node2 is None or (node1 and node1.val < node2.val):
                ans.append(node1.val)
                node1 = self.safeNext(gen1)
            elif node1 is None or (node2 and node2.val < node1.val):
                ans.append(node2.val)
                node2 = self.safeNext(gen2)
            else:
                ans.append(node1.val)
                ans.append(node2.val)
                node1, node2 = self.safeNext(gen1), self.safeNext(gen2)
        return ans