"""
Python3 solution with O(1) and O(n) space [two stacks]

We use a native Python stack (list) to implement the pop,push and top
operations. They all achieve the expected O(1), and space is O(n).

For the getMin operation, we use an additional array that will keep track of
the minimum up to certain position i-th; that is

minpos[i] = min(arr[:i])

This second array (stack) can be updated in O(1) as well, because

minpos[i+1] = min(arr[i+1], minpos[i])

hence, we use above formulate inside push implementation. When popping,
we just need to pop from both stacks simultaneously; such that the last
position of minpos will always give global minimum.

So we are able to maintain the complexities of a single stack, even after
considering the extra costs of this minpos.

"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.minpos = []

    def push(self, x):
        self.stack.append(x)
        prev = self.minpos[-1] if self.minpos else x
        self.minpos.append(min(prev, x))

    def pop(self):
        self.stack.pop()
        self.minpos.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minpos[-1]

