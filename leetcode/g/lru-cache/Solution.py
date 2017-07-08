from collections import deque


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.valPos = dict()
        self.keys = deque()
        self.capacity = capacity
        self.shift = 0

    def _moveToRightEnd(self, key, value=None):
        i, j = self.valPos[key][1], len(self.keys) - 1
        i, j = i - self.shift, j
        self.keys[i], self.keys[j] = self.keys[j], self.keys[i]
        if value is not None:
            self.valPos[key][0] = value
        self.valPos[key][0] = j
        self.valPos[self.keys[i]][1] = i

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.valPos:
            self._moveToRightEnd(key)
            return self.valPos[key][0]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.valPos:
            self._moveToRightEnd(key, value)
        else:
            if len(self.keys) == self.capacity:
                delKey = self.keys.popleft()
                del self.valPos[delKey]
                self.shift += 1
            self.keys.append(key)
            self.valPos[key] = [value, len(self.keys) - 1 + self.shift]

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