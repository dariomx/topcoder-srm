from random import randint
class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.pos = dict()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            return False
        else:
            self.arr.append(val)
            self.pos[val] = len(self.arr) - 1
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            i = self.pos[val]
            last_i = len(self.arr) - 1
            last_val = self.arr[last_i]
            self.pos[val], self.pos[last_val] = last_i, i
            self.arr[i], self.arr[last_i] = last_val, val
            self.arr.pop()
            del self.pos[val]
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        i = randint(0, len(self.arr) - 1)
        return self.arr[i]


soln = RandomizedSet()
print(soln.insert(1))
print(soln.remove(2))
print(soln.insert(2))
print(soln.remove(1))
print(soln.insert(2))

