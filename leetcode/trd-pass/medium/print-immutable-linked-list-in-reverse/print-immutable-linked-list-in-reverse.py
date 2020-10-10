class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.getNext()
        while stack:
            node = stack.pop()
            node.printValue()