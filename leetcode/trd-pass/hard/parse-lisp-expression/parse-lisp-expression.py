from operator import add, mul as mult


class Solution:
    def __init__(self):
        self.let = lambda x: x
        self.opers = {'add': add, 'mult': mul, 'let': self.let}

    def parseAlphaNum(self, expr, i):
        name = expr[i]
        i += 1
        while i < len(expr) and expr[i].isalnum():
            name += expr[i]
            i += 1
        return name, i - 1

    def parseSign(self, expr, i):
        if expr[i] == '-':
            sign = -1
            i += 1
        else:
            sign = +1
        return sign, i

    def resolve(self, varname, scopes):
        for sco in reversed(scopes):
            value = sco.get(varname, None)
            if value is not None:
                return value
        raise ValueError('Could not resolve variable %s' % varname)

    def setVar(self, ops, args, scopes):
        if ops and ops[-1] == self.let and len(args[-1]) > 1 and type(
                args[-1][-2]) == str:
            value, varname = args[-1].pop(), args[-1].pop()
            scopes[-1][varname] = value

    def handleVarname(self, expr, i, ops, args, scopes, spc):
        varname, i = self.parseAlphaNum(expr, i)
        isBinding = ops[-1] == self.let and spc[-1] % 2 == 1 and \
                    not (i < len(expr) - 1 and expr[i + 1] == ')')
        if isBinding:
            args[-1].append(varname)
        else:
            value = self.resolve(varname, scopes)
            args[-1].append(value)
        return not isBinding, i

    def evaluate(self, expr: str) -> int:
        ops, args, scopes, spc = [None], [[]], [{}], [0]
        i = 0
        while i < len(expr):
            c = expr[i]
            justEval = False
            if c == '(':
                opname, i = self.parseAlphaNum(expr, i + 1)
                ops.append(self.opers[opname])
                args.append([])
                scopes.append({})
                spc.append(0)
            elif c == ')':
                f, xs = ops.pop(), args.pop()
                value = f(*xs)
                args[-1].append(value)
                scopes.pop()
                spc.pop()
                justEval = True
            elif c.isalpha():
                justEval, i = self.handleVarname(expr, i, ops, args, scopes,
                                                 spc)
            elif c == '-' or c.isdigit():
                sign, i = self.parseSign(expr, i)
                valueStr, i = self.parseAlphaNum(expr, i)
                args[-1].append(sign * int(valueStr))
                justEval = True
            elif c == ' ':
                spc[-1] += 1
            if justEval:
                self.setVar(ops, args, scopes)
            i += 1
        return args[-1][0]
