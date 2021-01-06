from collections import deque
from typing import List

from math import inf


class Image:
    def __init__(self, grid):
        n = len(grid)
        self.bits = deque([0] * n)
        for i in range(n):
            for j in range(n):
                self.bits[i] |= grid[i][n - 1 - j] << (n + j)
        self.n = n
        self.mask = ((1 << n) - 1) << n
        self.inv = {'L': 'R', 'R': 'L', 'U': 'D', 'D': 'U'}

    def left(self):
        for i in range(self.n):
            self.bits[i] = (self.bits[i] << 1)

    def right(self):
        for i in range(self.n):
            self.bits[i] = (self.bits[i] >> 1)

    def up(self, last=0):
        self.bits.popleft()
        self.bits.append(last)

    def down(self, fst=0):
        self.bits.pop()
        self.bits.appendleft(fst)

    def op(self, opcode, fst=0, last=0):
        if opcode == 'L':
            self.left()
        elif opcode == 'R':
            self.right()
        elif opcode == 'U':
            self.up(last)
        else:
            self.down(fst)

    def rollback(self, opcode, fst, last):
        self.op(self.inv[opcode], fst, last)

    def hash(self):
        return tuple(self.bits)

    def is_zero(self):
        return sum((row & self.mask for row in self.bits)) == 0

    def overlap(self, other):
        cnt = 0
        for i in range(self.n):
            ro = (self.bits[i] & self.mask) & (other.bits[i] & self.mask)
            cnt += format(ro, '0b').count('1')
        return cnt

    def fstLast(self):
        return self.bits[0], self.bits[-1]


class Solution:
    def largestOverlap(self, img1: List[List[int]],
                       img2: List[List[int]]) -> int:
        def rec(cur):
            nonlocal ans
            key = cur.hash()
            if key in cache:
                return
            cache.add(key)
            ans = max(ans, cur.overlap(target))
            if cur.is_zero():
                return
            fst, last = cur.fstLast()
            for opcode in 'LRUD':
                cur.op(opcode)
                rec(cur)
                cur.rollback(opcode, fst, last)

        # main
        cache = set()
        ans = -inf
        target = Image(img2)
        rec(Image(img1))
        return ans
