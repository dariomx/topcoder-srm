class Solution:
    def racecar(self, target: int) -> int:
        sign = lambda x: +1 if x >= 0 else -1
        log2 = int(log(target + 1) / log(2))
        queue = deque([(0, 1, 0)] + \
                      [(2 ** k - 1, 2 ** k, k) for k in range(1, log2 + 1)])
        visited = set(queue)
        while queue:
            x, speed, steps = queue.popleft()
            if abs(x - target) > target:
                continue
            if x == target:
                return steps
            for child in ((x + speed, speed * 2, steps + 1),
                          (x, -1 * sign(speed), steps + 1)):
                if child not in visited:
                    visited.add(child)
                    queue.append(child)
