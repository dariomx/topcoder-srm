from abc import ABC, abstractmethod
from operator import add, sub, mul, floordiv as div


class Node(ABC):
    @abstractmethod
    def evaluate(self) -> int:
        pass


class ExprNode(Node):
    def __init__(self, postfix: List[str]):
        self.postfix = postfix
        self.op = {'+': add, '-': sub, '*': mul, '/': div}

    def evaluate(self) -> int:
        stack = []
        for tok in self.postfix:
            if tok in self.op:
                op = self.op[tok]
                y, x = stack.pop(), stack.pop()
                res = op(x, y)
            else:
                res = int(tok)
            stack.append(res)
        return stack[0]


class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        return ExprNode(postfix)

