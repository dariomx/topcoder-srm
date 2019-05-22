class Solution:
    def leafSimilar(self, root1, root2):
        def leafSeq(root):
            if root:
                if not root.left and not root.right:
                    yield root.val
                else:
                    yield from leafSeq(root.left)
                    yield from leafSeq(root.right)

        return list(leafSeq(root1)) == list(leafSeq(root2))
