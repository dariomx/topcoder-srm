from collections import defaultdict

class Solution:
    def findDuplicate(self, paths):
        group = defaultdict(lambda: [])
        for p in paths:
            tok = p.split()
            dir = tok[0]
            for i in range(1, len(tok)):
                file, cont = tok[i].replace("("," ").replace(")","").split()
                group[cont].append(dir + "/" + file)
        return list(filter(lambda g: len(g) > 1, group.values()))