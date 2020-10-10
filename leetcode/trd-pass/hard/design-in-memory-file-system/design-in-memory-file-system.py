class File:
    def __init__(self, name):
        self.name = name


class RegularFile(File):
    def __init__(self, name):
        super().__init__(name)
        self.contents = ''

    def addContent(self, cont):
        self.contents += cont

    def getContent(self):
        return self.contents


class Directory(File):
    def __init__(self, name):
        super().__init__(name)
        self.entries = dict()

    def ls(self, path):
        if not path:
            return sorted(self.entries.keys())
        else:
            ename = path.pop()
            if type(self.entries[ename]) == RegularFile:
                return [ename]
            else:
                return self.entries[ename].ls(path)

    def mkdir(self, path):
        if not path:
            return
        ename = path.pop()
        if ename not in self.entries:
            self.entries[ename] = Directory(ename)
        self.entries[ename].mkdir(path)

    def addContent(self, path, cont):
        ename = path.pop()
        if not path:
            if ename not in self.entries:
                self.entries[ename] = RegularFile(ename)
            self.entries[ename].addContent(cont)
        else:
            if ename not in self.entries:
                self.entries[ename] = Directory(ename)
            self.entries[ename].addContent(path, cont)

    def getContent(self, path):
        ename = path.pop()
        if not path:
            return self.entries[ename].getContent()
        else:
            return self.entries[ename].getContent(path)


class FileSystem:
    def __init__(self):
        self.root = Directory('/')

    def _convPath(self, path):
        path = path[1:]
        if path and path[-1] == '/':
            path = path[:-1]
        if path == '':
            return []
        else:
            return path.split('/')[::-1]

    def ls(self, path: str) -> List[str]:
        path = self._convPath(path)
        return self.root.ls(path)

    def mkdir(self, path: str) -> None:
        path = self._convPath(path)
        self.root.mkdir(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        path = self._convPath(filePath)
        self.root.addContent(path, content)

    def readContentFromFile(self, filePath: str) -> str:
        path = self._convPath(filePath)
        return self.root.getContent(path)
