from operator import add, sub

OPER = {'+': add, '-': sub}


class Solution:
    def calculate(self, s: str) -> int:
        ops = []
        args = []
        num = ''
        for c in (s + ' '):
            if c.isdigit():
                num += c
            else:
                if len(num) > 0:
                    args.append(int(num))
                    num = ''
                drop_par = False
                if c == ')' and ops[-1] == '(':
                    ops.pop()
                    drop_par = True
                elif c == '(':
                    ops.append(c)
                if len(args) >= 2 and len(ops) >= 1 and ops[-1] in '+-':
                    y = args.pop()
                    x = args.pop()
                    op = OPER[ops.pop()]
                    args.append(op(x, y))
                if c in '+-':
                    ops.append(c)
                elif c == ')' and not drop_par:
                    ops.pop()
        return args[0]

