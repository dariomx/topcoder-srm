from math import inf


def drawtree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1

    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y - 20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x - dx, y - 60, dx / 2)
            jumpto(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 2)

    import turtle
    t = turtle.Turtle()
    t.speed(0);
    turtle.delay(0)
    h = height(root)
    jumpto(0, 30 * h)
    draw(root, 0, 30 * h, 40 * h)
    t.hideturtle()
    turtle.mainloop()


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return '[%d]' % self.val

    def isLeaf(self):
        return self.left is None and self.right is None

    def maxCost(self, n):
        ret = 0
        cnt = 0
        stack = [(self, 0)]
        while stack:
            node, cost = stack.pop()
            if node.isLeaf():
                ret = max(ret, cost)
            cost += node.val
            cnt += 1
            for child in (node.left, node.right):
                if child:
                    stack.append((child, cost))
        ret = ret if cnt == n else inf
        return ret


LEFT = 1
RIGHT = 2


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        def rec(start, end, side, parent):
            nonlocal root, ans
            if start > end:
                None
            else:
                for i in range(start, end + 1):
                    node_i = Node(i)
                    if parent:
                        if side == LEFT:
                            parent.left = node_i
                        else:
                            parent.right = node_i
                    else:
                        root = node_i
                    rec(start, i - 1, LEFT, node_i)
                    rec(i + 1, end, RIGHT, node_i)
                    print('dead')
                ans = min(ans, root.maxCost(n))

        # main
        root = None
        ans = inf
        rec(1, n, None, None)
        return ans


print(Solution().getMoneyAmount(10))
