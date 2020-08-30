class Solution:
    def getSize(self, head):
        node = head
        size = 0
        while node:
            size += 1
            node = node.next
        return size

    def getDecimalValue(self, head: ListNode) -> int:
        size = self.getSize(head)
        pow2 = 1 << (size - 1)
        ans = 0
        node = head
        while node:
            ans += pow2 * node.val
            pow2 >>= 1
            node = node.next
        return ans
