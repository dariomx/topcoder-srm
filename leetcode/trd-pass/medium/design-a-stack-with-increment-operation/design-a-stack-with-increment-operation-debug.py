class CustomStack:
    def __init__(self, maxSize: int):
        self.stack = [0] * maxSize
        self.inc = [0] * maxSize
        self.idx = -1

    def push(self, x: int) -> None:
        if self.idx < len(self.stack) - 1:
            self.idx += 1
            self.stack[self.idx] = x

    def pop(self) -> int:
        ret = -1
        if self.idx >= 0:
            ret = self.stack[self.idx] + self.inc[self.idx]
            if self.idx - 1 >= 0:
                self.inc[self.idx - 1] += self.inc[self.idx]
            self.stack[self.idx] = 0
            self.inc[self.idx] = 0
            self.idx -= 1
        return ret

    def increment(self, k: int, val: int) -> None:
        if self.idx >= 0:
            i = min(k-1, self.idx)
            self.inc[i] += val

# main
ops = ["CustomStack","increment","pop","increment","push","increment","pop","push","push","push","push","push","increment","pop","pop","push","push","push","push","push","increment","push","push","increment","increment","pop","increment","push","increment","push","push","pop","push","push","pop","push","push","pop","pop","push","pop","push","push","push","push","push","push","increment","pop","push","pop","push","push","push","increment","pop","increment","push","push","push","push","push","push","push","push","increment","push","push","push","push","push","push","push","push","pop","push","increment","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","pop","push","push","push","pop","increment","push","push","increment","pop","pop","pop","pop","push","push","push","pop","push","push","push","push","push","pop","push","push","push","push","push","push","push","push","increment","increment","increment","pop","increment","increment","push","increment","push","push","push","push","push","push","push","push","push","push","push","push","push","pop","increment","pop","push","increment","push","pop","increment","push","increment","increment","pop","push","pop","pop","push","pop","pop","push","increment","push","push","increment","push","push","push","push","pop","push","push","pop","push","push","push","push","push","push","pop","increment","push","push","push","push","pop","push","push","increment","increment","push","push","push","push","pop","increment","push","increment","push","pop","push","pop","push","push","push","push","push","push","push","push","pop","push","push","push","push","push","push","push","push","push","pop","push","push","pop","push","increment","push","increment","push","push","increment","push","increment","increment","push","push","push","push","push","push","push","increment","push","push","push","push","increment","push","increment","pop","push","push","increment","pop","pop","increment","push","increment","push","increment","increment","push","push","pop","push","pop","push","push","push","push","push","pop","pop","push","push","push","push","push","push","push","push","pop"]
args = [[137], [6, 45], [], [2, 29], [60], [2, 54], [], [96], [19], [60], [90], [55], [9, 53], [], [], [14], [96], [65], [14], [34], [4, 31], [47], [59], [1, 61], [9, 98], [], [8, 69], [86], [7, 56], [86], [14], [], [93], [18], [], [1], [39], [], [], [41], [], [48], [58], [21], [36], [92], [46], [5, 62], [], [57], [], [42], [90], [100], [8, 54], [], [2, 75], [89], [57], [35], [51], [95], [48], [55], [28], [8, 39], [28], [100], [39], [36], [84], [82], [96], [69], [], [57], [4, 83], [64], [48], [58], [25], [30], [66], [45], [30], [14], [54], [56], [6], [97], [91], [16], [], [85], [51], [100], [], [8, 48], [68], [20], [3, 4], [], [], [], [], [35], [24], [85], [], [79], [58], [62], [62], [99], [], [97], [32], [43], [20], [7], [56], [48], [15], [6, 68], [10, 86], [10, 83], [], [7, 88], [10, 78], [40], [7, 94], [27], [7], [63], [2], [57], [82], [31], [58], [3], [77], [37], [68], [3], [], [3, 81], [], [14], [7, 33], [84], [], [5, 23], [35], [5, 51], [9, 60], [], [73], [], [], [10], [], [], [80], [2, 46], [19], [32], [4, 52], [22], [32], [35], [45], [], [19], [8], [], [44], [54], [38], [28], [36], [94], [], [8, 68], [13], [34], [72], [60], [], [68], [29], [8, 73], [5, 62], [73], [64], [25], [77], [], [8, 86], [78], [1, 69], [94], [], [98], [], [8], [93], [7], [55], [8], [14], [78], [71], [], [91], [65], [5], [69], [4], [34], [100], [46], [12], [], [6], [81], [], [23], [5, 16], [16], [8, 97], [14], [84], [3, 97], [10], [2, 68], [4, 84], [54], [58], [4], [65], [79], [10], [17], [2, 68], [1], [53], [54], [3], [9, 75], [35], [6, 63], [], [15], [88], [6, 86], [], [], [10, 51], [27], [10, 86], [50], [4, 63], [2, 91], [13], [26], [], [82], [], [46], [39], [50], [84], [41], [], [], [18], [70], [18], [34], [44], [68], [82], [67], []]
stack = CustomStack(args[0][0])
for op, arg in zip(ops[1:], args[1:]):
    if op == "push":
        stack.push(arg[0])
    elif op == "pop":
        aver = stack.pop()
        print(aver)
    else:
        k, val = arg
        stack.increment(k, val)


