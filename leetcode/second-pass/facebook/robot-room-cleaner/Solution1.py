# by simply turning the iterative dfs into recursive one,
# we do not need to always rollback to origin (got this
# hint from one of the forum solutions and just adapted my version)
#
# this is still not optimal cause it rollsback each direction
# individually, and i guess we can leverage the rotation.

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

    def get_nei(self, pos, robot):
        x, y = pos
        for dir in (UP, LEFT, RIGHT, DOWN):
            if self.apply(dir, robot):
                yield ((x + dir[0], y + dir[1]), dir)
                self.apply(inv[dir], robot)

    def dfs(self, pos, visited, robot):
        if pos in visited:
            return
        visited.add(pos)
        robot.clean()
        for nei, dir in self.get_nei(pos, robot):
            self.dfs(nei, visited, robot)

    def cleanRoom(self, robot):
        start = (0, 0)
        visited = set()
        self.dfs(start, visited, robot)
