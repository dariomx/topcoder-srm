E = 0
S = 1
F = 2


class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.grid = defaultdict(lambda: E)
        self.grid[0, 0] = S
        self.snake = deque([(0, 0)])
        self.score = 0
        self.food = deque(food)
        self._nextFood()

    def _nextFood(self):
        if self.food:
            i, j = self.food.popleft()
            self.grid[i, j] = F

    def _nextPos(self, direction):
        i, j = self.snake[-1]
        if direction == 'U':
            i -= 1
        elif direction == 'D':
            i += 1
        elif direction == 'L':
            j -= 1
        else:
            j += 1
        return i, j

    def move(self, direction: str) -> int:
        i, j = self._nextPos(direction)
        if not (0 <= i < self.height and 0 <= j < self.width):
            ret = -1
        else:
            if self.grid[i, j] == F:
                self.score += 1
                self._nextFood()
            else:
                x, y = self.snake.popleft()
                self.grid[x, y] = E
            if self.grid[i, j] == S:
                ret = -1
            else:
                self.snake.append((i, j))
                self.grid[i, j] = S
                ret = self.score
        return ret
