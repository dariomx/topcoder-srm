from itertools import izip, imap

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        grid = [[0]*n for _ in xrange(m)]
        goodIdxs = lambda (i,j): (0 <= i < m and 0 <= j < n)
        diag  = [(-1,-1), (-1,1), (1,1), (1,-1)]
        cross = [(-1,0), (0,1), (1,0), (0,-1)]
        perim = [coord for pair in izip(diag,cross) for coord in pair]
        #
        def getNeig(x, y, deltas, startZero=False):
            incr = lambda (i,j): (x+i, y+j)
            if startZero:
                neig = map(incr, deltas)
                k = 0
                while k < len(neig) and \
                  goodIdxs(neig[k]) and \
                  grid[neig[k][0]][neig[k][1]] == 1:
                    k += 1
                if k == len(neig):
                    k = 0
                return neig[k:] + neig[:k]
            else:
                return imap(incr, deltas)
        #
        def debug(x, y, cnt, numIslands):
            print("x,y = %d,%d\t%d != %d" % (x, y, cnt, numIslands))
            print("\n".join(imap(lambda row: "".join(imap(str, row)), grid)))
        #
        def countIslands():
            cnt = 0
            land = set()
            for i in xrange(m):
                for j in xrange(n):
                    if grid[i][j] == 1:
                        land.add((i,j))
            visited = set()
            while land:
                start = land.pop()
                cnt += 1
                stack = [start]
                visited.clear()
                while stack:
                    x, y = stack.pop()
                    if (x,y) not in visited:
                        visited.add((x,y))
                        for i, j in getNeig(x, y, cross):
                            if goodIdxs((i,j)) and \
                                     grid[i][j] > 0 and (i,j) in land:
                                stack.append((i,j))
                                land.remove((i,j))
            return cnt
        #
        result = []
        numIslands = 0
        ids = set()
        for k in xrange(0, len(positions)):
            x, y = positions[k]
            if (x,y) == (3,17):
                print("darkness")
                debug(x, y, countIslands(), numIslands)
            grid[x][y] = 1
            numIslands += 1
            islandId = 1
            for i, j in getNeig(x, y, perim, True):
                if goodIdxs((i,j)) and grid[i][j] == 1:
                    grid[i][j] = islandId
                else:
                    islandId += 1
            ids.clear()
            for i, j in getNeig(x, y, cross):
                if goodIdxs((i,j)) and grid[i][j] > 0:
                    ids.add(grid[i][j])
            numIslands -= len(ids)
            result.append(numIslands)
            for i, j in getNeig(x, y, perim):
                if goodIdxs((i,j)) and grid[i][j] > 0:
                    grid[i][j] = 1
            if m == 7 and n == 32:
                cnt = countIslands()
                if cnt != numIslands:
                    debug(x, y, cnt, numIslands)
        return result

m, n = 7, 32
positions = \
[
 [6,16],[3,6],[2,2],[2,9],[1,12],[1,6],[5,17],[4,1],[2,17],[5,27],
 [0,21],[3,7],[6,26],[3,0],[6,18],[6,8],[1,11],[6,30],[0,8],[3,16],
 [0,3],[4,15],[3,15],[4,17],[3,4],[0,27],[2,4],[0,1],[2,20],[6,19],
 [4,26],[1,15],[3,3],[0,14],[5,16],[5,28],[4,24],[4,13],[6,6],[2,14],
 [2,22],[1,26],[6,27],[5,23],[3,13],[5,15],[4,2],[5,30],[0,11],[3,22],
 [2,1],[6,7],[4,10],[2,5],[6,0],[6,24],[3,27],[4,19],[4,6],[3,17],
 [2,15]
]
print(Solution().numIslands2(m, n, positions))