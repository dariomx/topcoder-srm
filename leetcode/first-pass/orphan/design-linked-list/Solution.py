class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def _get(self, index):
        node = self.head
        for _ in range(index):
            if not node:
                return None
            node = node.next
        return node

    def get(self, index):
        node = self._get(index)
        if node:
            return node.val
        else:
            return -1

    def addAtHead(self, val):
        node = Node(val)
        if self.head:
            self.head.prev = node
            node.next = self.head
            self.head = node
        else:
            self.head = self.tail = node
        self.size += 1

    def addAtTail(self, val):
        node = Node(val)
        node.prev = self.tail
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node
        self.size += 1

    def addAtIndex(self, index, val):
        if index == self.size:
            self.addAtTail(val)
        elif index < self.size:
            node = self._get(index)
            new = Node(val)
            new.next = node
            new.prev = node.prev
            if node.prev:
                node.prev.next = new
            node.prev = new
            if node == self.head:
                self.head = new
            self.size += 1

    def deleteAtIndex(self, index):
        node = self._get(index)
        if node:
            if node.prev:
                node.prev.next = node.next
            else:
                self.head = node.next
            if node.next:
                node.next.prev = node.prev
            else:
                self.tail = node.prev
            self.size -= 1
