class CleanerRobot:
    def move(self, dir):
        return False

    def clean(self):
        None

class Solution:
    def __init__(self):
        self.inverseDir = {
            'F': 'B',
            'B': 'F',
            'L': 'R',
            'R': 'L'
        }

    def movePath(self, path, cleaner):
        for dir in path:
            cleaner.move(dir)

    def rollbackPath(self, path, cleaner):
        for dir in reversed(path):
            cleaner.move(self.inverseDir[dir])

    def cleanRoom(self, cleaner):
        stack = [[]]
        while stack:
            path = stack.pop()
            for dir in self.inverseDir.iterkeys():
                if cleaner.move(dir):
                    self.rollbackPath([dir], cleaner)
                    stack.append(path + [dir])
            self.rollbackPath(path, cleaner)
                        