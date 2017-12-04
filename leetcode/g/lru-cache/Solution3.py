class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


class List:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def append(self, node):
        if self.size == 0:
            self.first = self.last = node
        else:
            node.next = node.prev = None
            self.last.next = node
            node.prev = self.last
            self.last = node
        self.size += 1

    def popLeft(self):
        if self.size == 0:
            raise ValueError("empty list")
        else:
            ret = self.first
            self.first = self.first.next
            if self.first:
                self.first.prev = None
            self.size -= 1
            return ret

    def moveToLast(self, node):
        if node == self.first:
            self.popLeft()
        else:
            node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            else:
                self.last = node.prev
            self.size -= 1
        self.append(node)

    def __len__(self):
        return self.size


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.list = List()
        self.nodeVal = dict()
        self.capacity = capacity

    def _movetoLast(self, key, value=None):
        node = self.nodeVal[key][0]
        self.list.moveToLast(node)
        if value is not None:
            self.nodeVal[key][1] = value

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.nodeVal:
            self._movetoLast(key)
            return self.nodeVal[key][1]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.nodeVal:
            self._movetoLast(key, value)
        else:
            if len(self.list) == self.capacity:
                delNode = self.list.popLeft()
                del self.nodeVal[delNode.key]
            self.list.append(Node(key))
            self.nodeVal[key] = [self.list.last, value]


soln = LRUCache(3)
soln.put(1, 1)
soln.put(2, 2)
soln.put(3, 3)
soln.put(4, 4)
print(soln.get(4))
print(soln.get(3))
print(soln.get(2))
print(soln.get(1))
soln.put(5, 5)
print(soln.get(1))
print(soln.get(2))
print(soln.get(3))
print(soln.get(4))
print(soln.get(5))
