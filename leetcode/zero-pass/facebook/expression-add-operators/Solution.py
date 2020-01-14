from operator import add, sub, mul

app = lambda x, y: x * 10 + y

op_sym = {add: '+', sub: '-', mul: '*', app: ''}


class State:
    def __init__(self, x=0):
        self.add_left = 0
        self.add_op = None
        self.mul_left = x
        self.mul_op = None
        self.mul_right = 0
        self.exp = str(x)

    def copy(self):
        other = State()
        other.add_left = self.add_left
        other.add_op = self.add_op
        other.mul_left = self.mul_left
        other.mul_op = self.mul_op
        other.mul_right = self.mul_right
        other.exp = self.exp
        return other

    def eval(self):
        if self.mul_op:
            add_right = mul(self.mul_left, self.mul_right)
            self.mul_left = 0
            self.mul_op = None
            self.mul_right = 0
        else:
            add_right = self.mul_left
            self.mul_left = 0

        if self.add_op:
            res = self.add_op(self.add_left, add_right)
            self.add_left = 0
            self.add_op = None
        else:
            res = add_right
        return res

    def extend(self, op, x):
        if op == app:
            if self.mul_op:
                self.mul_right = app(self.mul_right, x)
            else:
                self.mul_left = app(self.mul_left, x)
        elif op == mul:
            if self.mul_op:
                self.mul_left *= self.mul_right
                self.mul_right = x
            else:
                if self.mul_left > 0:
                    self.mul_right = x
                else:
                    self.mul_left = x
                self.mul_op = mul
        else:
            self.add_left = self.eval()
            self.add_op = op
            self.mul_left = x
        self.exp += op_sym[op] + str(x)

    def is_good(self):
        num = ""
        bad_num = lambda n: n and len(n) != len(str(int(n)))
        for i in range(len(self.exp)):
            if self.exp[i].isdigit():
                num += self.exp[i]
            else:
                if bad_num(num):
                    return False
                num = ""
        if bad_num(num):
            return False
        return True

    def __str__(self):
        vals = (self.add_left,
                self.add_op,
                self.mul_left,
                self.mul_op,
                self.mul_right,
                self.exp)
        return "(%d %s %d %s %d, %s)" % vals


class Solution:
    def addOperators(self, num, target):
        n = len(num)
        ans = []

        def rec(i, state):
            if i == n:
                if state.eval() == target and state.is_good():
                    ans.append(state.exp)
            else:
                x = int(num[i])
                for op in op_sym:
                    op_state = state.copy()
                    op_state.extend(op, x)
                    rec(i + 1, op_state)

        if not num:
            return []
        else:
            rec(1, State(int(num[0])))
            return ans


num = "1000000009"
target = 9
print(Solution().addOperators(num, target))