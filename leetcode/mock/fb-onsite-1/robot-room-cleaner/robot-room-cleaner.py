# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

MOVE = 1
RIGHT = 2
LEFT = 3
CLEAN = 4


class Solution:
    def get_neighbors(self, node, paths, robot):
        x, y = node
        nei = []
        if robot.move():
            nei.append(x - 1, y)
            paths[x - 1, y] = paths[node] + [MOVE]
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()
        robot.turnLeft()
        if robot.move():
            nei.append(x, y - 1)
            path[x, y - 1] = paths[node] + [LEFT, MOVE]
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnLeft()
        robot.turnRight()
        if robot.move():
            nei.append(x, y + 1)
            path[x, y + 1] = paths[node] + [RIGHT, MOVE]
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
        robot.turnRight()
        robot.turnRight()
        if robot.move():
            nei.append(x + 1, y)
            path[x + 1, y] = paths[node] + [RIGHT, RIGHT, MOVE]
            robot.turnRight()
            robot.turnRight()
            robot.move()
        return nei

    def robotCmd(self, robot, cmd):
        if cmd == MOVE:
            robot.move()
        elif cmd == RIGHT:
            robot.turnRight()
        elif cmd == LEFT:
            robot.turnLeft()
        else:
            robot.clean()

    def gotoNode(self, path, robot):
        for cmd in path:
            self.robotCmd(robot, cmd)

    def comebackNode(path, robot):

    def cleanRoom(self, robot):