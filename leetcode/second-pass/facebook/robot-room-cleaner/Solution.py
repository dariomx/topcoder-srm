UP = (-1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
DOWN = (1, 0)

inv = {UP: DOWN, DOWN: UP, LEFT: RIGHT, RIGHT: LEFT}


class Solution:
    def apply(self, dir, robot):
        ret = False
        if dir == UP:
            ret = robot.move()
        elif dir == LEFT:
            robot.turnLeft()
            ret = robot.move()
            robot.turnRight()
        elif dir == RIGHT:
            robot.turnRight()
            ret = robot.move()
            robot.turnLeft()
        else:
            robot.turnRight()
            robot.turnRight()
            ret = robot.move()
            robot.turnRight()
            robot.turnRight()
        return ret

    def follow_fwd(self, path, robot):
        for dir in path:
            self.apply(dir, robot)

    def follow_bkd(self, path, robot):
        for dir in reversed(path):
            self.apply(inv[dir], robot)

    def get_nei(self, pos, path, robot):
        x, y = pos
        self.follow_fwd(path, robot)
        robot.clean()
        for dir in (UP, LEFT, RIGHT, DOWN):
            if self.apply(dir, robot):
                yield ((x + dir[0], y + dir[1]), dir)
                self.apply(inv[dir], robot)
        self.follow_bkd(path, robot)

    def cleanRoom(self, robot):
        start = (0, 0)
        visited = set()
        stack = [(start, [])]
        while stack:
            pos, path = stack.pop()
            if pos in visited:
                continue
            visited.add(pos)
            for nei, dir in self.get_nei(pos, path, robot):
                stack.append((nei, path + [dir]))
