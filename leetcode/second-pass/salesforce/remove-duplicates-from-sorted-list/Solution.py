class Solution:
    def deleteDuplicates(self, head):
        if head is None:
            return None
        prev = head
        node = head.next
        while node:
            if node.val == prev.val:
                prev.next = node.next
            else:
                prev = node
            node = node.next
        return head

