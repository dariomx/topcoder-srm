from operator import add, sub, mul, floordiv as div


class Solution:
    def __init__(self):
        self.OP = {'+': add, '-': sub, '*': mul, '/': div}
        self.PRIO = {'+': 1, '-': 1, '*': 2, '/': 2}

    def _parse_num(self, s, i):
        snum = ''
        while i < len(s) and s[i].isdigit():
            snum += s[i]
            i += 1
        return int(snum), i - 1

    def _unary_minus(self, s, i):
        return s[i] == '-' and s[i + 1].isdigit() and \
               (i == 0 or (i > 0 and (s[i - 1] in self.OP or s[i - 1] == '(')))

    def _read_next(self, s, i, opers, args):
        c = s[i]
        if c.isdigit():
            num, i = self._parse_num(s, i)
            args[-1].append(num)
        elif c == '(':
            opers.append([])
            args.append([])
        elif c == ')':
            self._eval(opers[-1], args[-1], final=True)
            opers.pop()
            res = args.pop()[0]
            args[-1].append(res)
        else:
            if c in self.OP:
                if self._unary_minus(s, i):
                    num, i = self._parse_num(s, i + 1)
                    args[-1].append(-num)
                else:
                    opers[-1].append(c)
        return i + 1

    def _eval(self, oper, arg, final=False):
        res = None
        if len(oper) > 1 and len(arg) > 1:
            op2 = oper.pop()
            op1 = oper.pop()
            z = arg.pop()
            y = arg.pop()
            if len(arg) > 0:
                x = arg.pop()
                if self.PRIO[op1] >= self.PRIO[op2]:
                    res = self.OP[op1](x, y)
                    arg.append(z)
                    oper.append(op2)
                else:
                    res = self.OP[op2](y, z)
                    arg.append(x)
                    oper.append(op1)
            elif self.PRIO[op1] >= self.PRIO[op2]:
                res = self.OP[op1](y, z)
                oper.append(op2)
            else:
                oper += [op1, op2]
                arg += [y, z]
        elif len(oper) > 0 and final:
            op1 = oper.pop()
            y = arg.pop()
            x = arg.pop()
            res = self.OP[op1](x, y)
        if res is not None:
            arg.append(res)

    def calculate(self, s: str) -> int:
        opers, args = [[]], [[]]
        i = 0
        s = s.replace(' ', '')
        while i < len(s):
            i = self._read_next(s, i, opers, args)
            print((opers, args))
            self._eval(opers[-1], args[-1])
        self._eval(opers[-1], args[-1], final=True)
        return args[0][0]