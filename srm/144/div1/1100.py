from operator import add

# partial soln cause i assumed that it was required to pass whole set of edges
# together, for each pass; rather seems like isolated segments can be passed
# as well.

class PenLift:
    def isHorizontal(self, l):
        (_,y1), (_,y2) = l
        return (y1 == y2)

    def parseLine(self, s):
        tks = map(int, s.split(" "))
        p1, p2 = (tks[0], tks[1]), (tks[2], tks[3])
        if self.isHorizontal((p1,p2)):
            sorter = lambda p: p[0]
        else:
            sorter = lambda p: p[1]
        p1 = min(p1, p2, key=sorter)
        p2 = max(p1, p2, key=sorter)
        return (p1,p2)

    # assumes both lines are either horizontal or vertical (and under same axis)
    def merge(self, l1, l2):
        print("merge l1=%s, l2=%s" % (str(l1),str(l2)))
        (x11, y11), (x12, y12) = l1
        (x21, y21), (x22, y22) = l2
        if self.isHorizontal(l1):
            if x11 <= x21 <= x12:
                return [((x11, y11), (x22, y11))]
            else:
                return [l1, l2]
        else:
            if y11 <= y21 <= y12:
                return [((x11, y11), (x11, y22))]
            else:
                return [l1, l2]

    # each line segment is already canonical (p1 <= p2), hence just sort
    # over the axis to allow a one time pass for merging (initially this
    # was going to be a foldr (reduce), but ended up needing iteration.
    def mergeAxis(self, lines, hor):
        if hor:
            sorter = lambda l: l[0][0]
        else:
            sorter = lambda l: l[0][1]
        newLines = []
        lines = sorted(lines, key=sorter)
        l1 = lines[0]
        for l in lines[1:]:
            merged = self.merge(l1, l)
            if len(merged) == 2:
                newLines.append(merged[0])
            l1 = merged[-1]
        newLines.append(l1)
        return newLines

    def mergeDirection(self, dir, hor):
        dirName = "hor" if hor else "ver"
        print("merging %s %s" % (dirName, str(dir)))
        for z in dir:
            print("merging %s[z] %s" % (dirName, str(dir[z])))
            dir[z] = self.mergeAxis(dir[z], hor)
            print("merging %s[z] %s" % (dirName, str(dir[z])))
        return dir

    def mergeLines(self, lines):
        hor = {}
        ver = {}
        for l in lines:
            (x1,y1),(x2,y2) = l
            if y1 == y2:
                if y1 in hor:
                    hor[y1].append(l)
                else:
                    hor[y1] = [l]
            else:
                if x1 in ver:
                    ver[x1].append(l)
                else:
                    ver[x1] = [l]
        return self.mergeDirection(hor, True),\
               self.mergeDirection(ver, False)

    def split(selfs, h, v):
        print("split: h=%s, v=%s" % (str(h),str(v)))
        (hx1,hy1),(hx2,_) = h
        (vx1,vy1),(vx2,vy2) = v
        if hx1 < vx1 < hx2 and vy1 < hy1 < vy2:
            print("splitting %s and %s" % (str(h),str(v)))
            hs = [((hx1,hy1),(vx1,hy1)), ((vx1,hy1),(hx2,hy1))]
            vs = [((vx1,vy1),(vx1,hy1)), ((vx1,hy1),(vx2,vy2))]
        else:
            hs,vs = [h], [v]
        print("hs = %s, vs = %s" % (str(hs),str(vs)))
        return hs,vs

    def splitLines(self, hor, ver):
        print("splitLines: hor=%s, ver=%s" % (str(hor),str(ver)))
        newHor = []
        for h in hor:
            h1 = h
            newVer = []
            for v in ver:
                print("h1 = %s, v = %s" % (str(h1),str(v)))
                sl = self.split(h1, v)
                print("sl = %s" % (str(sl)))
                if len(sl[0]) == 2:
                    newHor += [sl[0][0]]
                    newVer += sl[1]
                    h1 = sl[0][1]
                else:
                    newVer += sl[1]
                    h1 = sl[0][0]
                newHor.append(h1)
                ver = newVer
        return newHor,newVer

    def buildGraph(self, ss):
        lines = map(self.parseLine, ss)
        print("lines = %s" % (str(lines)))
        hor,ver = self.mergeLines(lines)
        print("hor1 = %s" % (str(hor)))
        print("ver1 = %s" % (str(ver)))
        hor,ver = self.splitLines(reduce(add, hor.values()),
                                  reduce(add, ver.values()))
        print("hor2 = %s" % (str(hor)))
        print("ver2 = %s" % (str(ver)))
        edges  = hor + ver
        graph = {}
        for (u,v) in edges:
            if u in graph:
                graph[u].append(v)
            else:
                graph[u] = [v]
            if v in graph:
                graph[v].append(u)
            else:
                graph[v] = [u]
        print("graph = %s" % str(graph))
        return graph

    def calcSCC(self, graph):
        white = 1
        gray = 2
        black = 3
        color = {}
        scc = {}
        iter = 0
        def dfs(u):
            color[u] = gray
            scc[iter].append(u)
            for v in graph[u]:
                if color[v] == white:
                    dfs(v)
            color[u] = black
        for u in graph:
            color[u] = white
        for u in graph:
            if color[u] == white:
                iter += 1
                scc[iter] = []
                dfs(u)
        print("scc = %s" % str(scc))
        return scc

    # on each scc, if u have 2k odd-parity nodes, then you have k
    # independent trails (paths) that cover together all edges. also,
    # the trails start and end on those odd-parity nodes.
    def numTimes(self, ss, t):
        graph = self.buildGraph(ss)
        scc = self.calcSCC(graph)
        lifts = len(scc.keys()) - 1
        for k in scc:
            odd = 0
            for u in scc[k]:
                odd += len(graph[u]) % 2
            lifts += (odd/2) * t - 1
        return lifts

