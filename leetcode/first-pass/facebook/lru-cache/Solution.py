class DLinkedNode:
    def __init__(self, key, val):
        self.prev = None
        self.key = key
        self.val = val
        self.next = None


class DLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def appendleft(self, node):
        if self.first:
            node.next = self.first
            self.first.prev = node
            self.first = node
        else:
            self.first = node
            self.last = node

    def pop(self):
        ret = self.last
        self.remove(self.last)
        return ret

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.first:
            self.first = node.next
        if node == self.last:
            self.last = node.prev
        node.prev = None
        node.next = None


class LRUCache:
    def __init__(self, capacity):
        self.list = DLinkedList()
        self.map = dict()
        self.capacity = capacity

    def get(self, key):
        if key in self.map:
            node = self.move_to_left(key)
            return node.val
        else:
            return -1

    def put(self, key, value):
        if key in self.map:
            node = self.move_to_left(key)
            node.val = value
        else:
            if len(self.map) == self.capacity:
                node = self.list.pop()
                del self.map[node.key]
            node = DLinkedNode(key, value)
            self.list.appendleft(node)
            self.map[key] = self.list.first

    def move_to_left(self, key):
        node = self.map[key]
        if node != self.list.first:
            self.list.remove(node)
            self.list.appendleft(node)
        return node
