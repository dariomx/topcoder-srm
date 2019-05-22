from operator import add, sub, mul, truediv as div

class Solution:
    def calculate(self, s: str) -> int:
        oper = {'+':add, '-':sub, '*':mul,
                '/': lambda x, y: int(div(x, y))}
        oper_prio = {'+':1, '-':1, '*':2, '/': 2}
        stack_op = []
        stack_arg = []
        i = 0
        while i < len(s):
            c = s[i]
            i += 1
            if c == " ":
                continue
            elif c in oper:
                stack_op.append(c)
            else:
                num = int(c)
                while i < len(s) and s[i].isdigit():
                    num = num*10 + int(s[i])
                    i += 1
                stack_arg.append(num)
            if len(stack_op) == 2 and len(stack_arg) == 3:
                op1, op2 = stack_op
                x, y, z = stack_arg
                stack_op = []
                stack_arg = []
                if oper_prio[op1] >= oper_prio[op2]:
                    stack_arg.append(oper[op1](x, y))
                    stack_arg.append(z)
                    stack_op.append(op2)
                else:
                    stack_arg.append(x)
                    stack_arg.append(oper[op2](y, z))
                    stack_op.append(op1)
        if stack_op:
            x, y = stack_arg
            return oper[stack_op.pop()](x, y)
        else:
            return stack_arg.pop()