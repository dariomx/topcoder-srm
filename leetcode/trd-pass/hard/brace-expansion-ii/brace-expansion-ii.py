union = lambda a, b: a | b
prod = lambda a, b: {x + y for x in a for y in b}


class Solution:
    def readStr(self, expr: str, i: int) -> Tuple[str, int]:
        s = ''
        while i < len(expr) and expr[i].isalpha():
            s += expr[i]
            i += 1
        return s, i - 1

    def eval(self, args: List[List[Set]], op: List[Callable]) -> None:
        f, xs = op.pop(), args.pop()
        if len(xs) == 1:
            res = xs[0]
        else:
            res = reduce(f, xs)
        args[-1].append(res)

    def braceExpansionII(self, expr: str) -> List[str]:
        args, op = [[], []], [prod]
        i, n = 0, len(expr)
        while i < n:
            c = expr[i]
            if c.isalpha():
                s, i = self.readStr(expr, i)
                args[-1].append({s})
            elif c == '{':
                args += [[], []]
                op += [union, prod]
            elif c == ',':
                self.eval(args, op)
                args.append([])
                op.append(prod)
            elif c in '}':
                self.eval(args, op)
                self.eval(args, op)
            i += 1
        self.eval(args, op)
        return sorted(args.pop()[0])
