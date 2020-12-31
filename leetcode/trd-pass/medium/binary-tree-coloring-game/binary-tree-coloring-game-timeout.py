class Solution:
    def getNodes(self, root):
        nodes = {}
        parent = {}
        stack = [(root, None)]
        while stack:
            node, par = stack.pop()
            nodes[node.val] = node
            parent[node] = par
            for child in (node.left, node.right):
                if child:
                    stack.append((child, node))
        return nodes, parent

    def play(self, turn, red, blue, nodes, parent, last_passed):
        key = (turn, tuple(red), tuple(blue))
        if key in self.cache:
            return self.cache[key]
        n = len(parent)
        if max(sum(red), sum(blue)) > n // 2:
            ret = sum(blue) > sum(red)
            self.cache[key] = ret
            return ret
        mine = red if turn == 0 else blue
        other = red if turn == 1 else blue
        passed = True
        for node in (nodes[i] for i in range(n) if mine[i]):
            for child in (node.left, node.right, parent[node]):
                if child and not mine[child.val] and not other[child.val]:
                    mine[child.val] = True
                    passed = False
                    ret = self.play(1 - turn, red, blue, nodes, parent, passed)
                    mine[child.val] = False
                    if ret:
                        break
        if passed:
            if last_passed:
                ret = sum(blue) > sum(red)
            else:
                ret = self.play(1 - turn, red, blue, nodes, parent, True)
        self.cache[key] = ret
        return ret

    def btreeGameWinningMove(self, root: TreeNode, n: int, i: int) -> bool:
        nodes, parent = self.getNodes(root)
        x = nodes[i]
        self.cache = {}
        red = [False] * (n + 1)
        red[i] = True
        blue = [False] * (n + 1)
        for j in range(1, n + 1):
            y = nodes[j]
            if x == y:
                continue
            else:
                blue[j] = True
                if self.play(0, red, blue, nodes, parent, False):
                    return True
                blue[j] = False
        return False
