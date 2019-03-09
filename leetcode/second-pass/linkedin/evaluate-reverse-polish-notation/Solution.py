from operator import add, sub, mul, truediv as div


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oper = {'+': add, '-': sub, '*': mul, '/': lambda x, y: int(div(x, y))}
        stack = []
        for tok in tokens:
            if tok in oper:
                y = stack.pop()
                x = stack.pop()
                res = oper[tok](x, y)
            else:
                res = int(tok)
            stack.append(res)
        return stack[0]
