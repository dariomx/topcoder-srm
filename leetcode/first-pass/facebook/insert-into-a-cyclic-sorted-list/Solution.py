from math import inf


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        new_node = Node(insertVal, None)
        if head is None:
            new_node.next = new_node
            return new_node
        elif head.next == head:
            if insertVal < head.val:
                new_node.next = head
                head.next = new_node
            else:
                head.next = new_node
                new_node.next = head
            return head
        else:
            node = head
            last = None
            max_val = -inf
            while True:
                if node.val >= max_val:
                    last = node
                    max_val = node.val
                node = node.next
                if node == head:
                    break
            node = last
            while insertVal > node.next.val:
                node = node.next
                if node == last:
                    break
            tmp = node.next
            node.next = new_node
            new_node.next = tmp
            return head
