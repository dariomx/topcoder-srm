"""
Python3 solution with O(n) and O(1) space

I feel bad about my verbose solution, after looking at other quite elegant
solutions. But well, here it goes.

1. Compute the length of the list (one pass)
2. Using the length split the list in two halves (discard middle if odd length)
3. Reverse second half
4. Compare first and second (reversed) halves

"""

class Solution:
    def get_len(self, head):
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        return n

    def reverse(self, head):
        node = head
        prev = None
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        return prev

    def split2(self, n, head):
        end1 = head
        for _ in range(n // 2 - 1):
            end1 = end1.next
        if n%2 == 1:
            start2 = end1.next.next
        else:
            start2 = end1.next
        end1.next = None
        return start2

    def isPalindrome(self, head):
        n = self.get_len(head)
        if n <= 1:
            return True
        start2 = self.split2(n, head)
        node2 = self.reverse(start2)
        node1 = head
        while node1 and node2:
            if node1.val != node2.val:
                return False
            node1 = node1.next
            node2 = node2.next
        return not node1 and not node2
