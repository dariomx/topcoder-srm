import java.util.Stack;

class Solution {
    private static final Position UP = new Position(-1, 0);
    private static final Position LEFT = new Position(0, -1);
    private static final Position RIGHT = new Position(0, 1);
    private static final Position DOWN = new Position(1, 0);

    private static final Position[] DIRS = {UP, LEFT, RIGHT, DOWN};

    private static final Map<Position, Position> INV;

    static {
        INV = new HashMap<>();
        INV.put(UP, DOWN);
        INV.put(DOWN, UP);
        INV.put(LEFT, RIGHT);
        INV.put(RIGHT, LEFT);
    }

    private boolean apply(Position dir, Robot robot) {
        boolean ret = false;
        if (dir == UP) {
            ret = robot.move();
        } else if (dir == LEFT) {
            robot.turnLeft();
            ret = robot.move();
            robot.turnRight();
        } else if (dir == RIGHT) {
            robot.turnRight();
            ret = robot.move();
            robot.turnLeft();
        } else {
            robot.turnRight();
            robot.turnRight();
            ret = robot.move();
            robot.turnRight();
            robot.turnRight();
        }
        return ret;
    }

    private void followFwd(List<Position> path, Robot robot) {
        for(Position dir: path) {
            apply(dir, robot);
        }
    }

    private void followBkd(List<Position> path, Robot robot) {
        for(int i=path.size()-1; i>=0; i--) {
            apply(INV.get(path.get(i)), robot);
        }
    }

    private void appendNei(Position pos,
                           List<Position> path,
                           Robot robot,
                           Stack<Tuple> stack) {
        followFwd(path, robot);
        robot.clean();
        for(int i=0; i<DIRS.length; i++) {
            Position dir = DIRS[i];
            if (apply(dir, robot)) {
                List<Position> newPath = new ArrayList<>(path);
                newPath.add(dir);
                stack.push(new Tuple(pos.add(dir), newPath));
                apply(INV.get(dir), robot);
            }
        }
        followBkd(path, robot);
    }

    public void cleanRoom(Robot robot) {
        Stack<Tuple> stack = new Stack<>();
        Position start = new Position(0, 0);
        stack.push(new Tuple(start, new ArrayList<>()));
        Set<Position> visited = new HashSet<>();
        while (!stack.isEmpty()) {
            Tuple tup = stack.pop();
            Position pos = tup.pos;
            List<Position> path = tup.path;
            if (visited.contains(pos)) {
                continue;
            }
            visited.add(pos);
            appendNei(pos, path, robot, stack);
        }
    }

    private static class Position {
        int x, y;

        public Position(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public Position add(Position pos) {
            return new Position(x + pos.x, y + pos.y);
        }

        @Override
        public boolean equals(Object obj) {
            if (obj instanceof Position) {
                Position other = (Position) obj;
                return x == other.x && y == other.y;
            } else {
                return false;
            }
        }

        @Override
        public int hashCode() {
            return 31*x + y;
        }
    }

    private static class Tuple {
        Position pos;
        List<Position> path;

        public Tuple(Position pos, List<Position> path) {
            this.pos = pos;
            this.path = path;
        }
    }
}