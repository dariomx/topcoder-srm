from collections import defaultdict

class TwoSum:
    def __init__(self):
        self.nums = defaultdict(lambda: 0)

    def add(self, number):
        self.nums[number] += 1

    def find(self, value):
        for x in self.nums:
            if value - x in self.nums:
                if x != value - x or self.nums[x] > 1:
                    return True
                else:
                    continue
        return False