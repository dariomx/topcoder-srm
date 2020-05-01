def has_cycle(head):
    slow = head
    fast = head.next
    while fast.next and slow != fast:
        slow = slow.next
        fast = fast.next.next
    return slow == fast
