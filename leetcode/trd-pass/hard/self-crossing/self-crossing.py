class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        dirs = {0: (0, +1), 1: (-1, 0), 2: (0, -1), 3: (+1, 0)}

        def move(y, z, i):
            dy, dz = dirs[i % 4]
            ny, nz = y + dy * x[i], z + dz * x[i]
            return y, z, ny, nz

        def add(seg):
            cache.append(seg)
            return seg[2], seg[3]

        def crosses(a, b):
            if a[1] == a[3] and b[1] != b[3]:
                return min(b[1], b[3]) <= a[1] <= max(b[1], b[3]) and \
                       min(a[0], a[2]) <= b[0] <= max(a[0], a[2])
            else:
                return (a[2], a[3]) in ((b[0], b[1]), (b[2], b[3]))

        cache = deque()
        y, z = 0, 0
        for i in range(len(x)):
            seg = move(y, z, i)
            for j in range(len(cache) - 1):
                if crosses(seg, cache[j]) or crosses(cache[j], seg):
                    return True
            y, z = add(seg)
            if len(cache) > 5:
                cache.popleft()
        return False
