class MyHashMap:
    def __init__(self):
        self.map = [-1] * 1000000

    def put(self, key, value):
        self.map[key] = value

    def get(self, key):
        return self.map[key]

    def remove(self, key):
        self.map[key] = -1
