class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class List:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def append(self, key):
        node = Node(key)
        if self.size == 0:
            self.first = self.last = node
        else:
            self.last.next = node
            self.last = node
        self.size += 1

    def popLeft(self):
        if self.size == 0:
            raise ValueError("empty list")
        else:
            ret = self.first
            self.first = self.first.next
            self.size -= 1
            return ret

    def swapLast(self, node):
        node.key, self.last.key = self.last.key, node.key

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

    def _swapLast(self, key, value=None):
        node = self.nodeVal[key][0]
        self.list.swapLast(node)
        self.nodeVal[key][0] = self.list.last
        self.nodeVal[node.key][0] = node
        if value is not None:
            self.nodeVal[key][1] = value
        self.nodeVal[key][1], self.nodeVal[node.key][1] = \
            self.nodeVal[node.key][1], self.nodeVal[key][1]

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.nodeVal:
            self._swapLast(key)
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
            self._swapLast(key, value)
        else:
            if len(self.list) == self.capacity:
                delNode = self.list.popLeft()
                del self.nodeVal[delNode.key]
            self.list.append(key)
            self.nodeVal[key] = [self.list.last, value]

            # Your LRUCache object will be instantiated and called as such:
            # obj = LRUCache(capacity)
            # param_1 = obj.get(key)
            # obj.put(key,value)

soln = LRUCache(3)
soln.put(1,1)
soln.put(2,2)
soln.put(3,3)
soln.put(4,4)
print(soln.get(4))
print(soln.get(3))
print(soln.get(2))
print(soln.get(1))
soln.put(5,5)
print(soln.get(1))
print(soln.get(2))
print(soln.get(3))
print(soln.get(4))
print(soln.get(5))