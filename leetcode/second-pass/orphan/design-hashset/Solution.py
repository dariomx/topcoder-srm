class MyHashSet:
    def __init__(self):
        self.hash = [False] * 1000001

    def add(self, key):
        self.hash[key] = True

    def remove(self, key):
        self.hash[key] = False

    def contains(self, key):
        return self.hash[key]
