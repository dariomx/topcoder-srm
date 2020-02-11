from operator import add, sub

OPER = {'+': add, '-': sub}


class Solution:
    def calc(self, s: str, start: int) -> int:
        ops = []
        args = []
        num = ''
        i = start
        while i < len(s):
            c = s[i]
            i += 1
            if c.isdigit():
                num += c
            else:
                if len(num) > 0:
                    args.append(int(num))
                    num = ''
                if len(args) >= 2 and len(ops) >= 1:
                    y = args.pop()
                    x = args.pop()
                    op = OPER[ops.pop()]
                    args.append(op(x, y))
                if c in '+-':
                    ops.append(c)
                elif c == '(':
                    res, i = self.calc(s, i)
                    args.append(res)
                elif c == ')':
                    break
        return args[0], i

    def calculate(self, s: str) -> int:
        return self.calc(s + ' ', 0)[0]

