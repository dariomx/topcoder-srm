class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def flat(head):
            node = head
            tail = head
            while node:
                if node.child:
                    chead, ctail = flat(node.child)
                    ctail.next = node.next
                    if node.next:
                        node.next.prev = ctail
                    node.next = chead
                    chead.prev = node
                    node.child = None
                    tail = ctail
                    node = ctail.next
                else:
                    tail = node
                    node = node.next
            return head, tail

        return flat(head)[0]
