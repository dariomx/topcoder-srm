class Solution(object):
    # dont see another way to avoid computing length all the time
    # damm, just saw the editorial 3rd soln ;-?
    def getIndex(self, head):
        node = head
        idx = []
        while node:
            idx.append(node)
            node = node.next
        return idx

    def sortedListToBST(self, head):
        def build(start, end):
            if start > end:
                return None
            else:
                mid = (start + end) // 2
                root = TreeNode(idx[mid].val)
                root.left = build(start, mid - 1)
                root.right = build(mid + 1, end)
                return root

        idx = self.getIndex(head)
        return build(0, len(idx) - 1)

