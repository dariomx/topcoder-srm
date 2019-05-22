class PhoneDirectory:

    def __init__(self, maxNumbers):
        self.used = set()
        self.avail = list(range(maxNumbers))

    def get(self):
        if self.avail:
            x = self.avail.pop()
            self.used.add(x)
        else:
            x = -1
        return x

    def check(self, number):
        return not (number in self.used)

    def release(self, number):
        if number in self.used:
            self.used.remove(number)
            self.avail.append(number)
