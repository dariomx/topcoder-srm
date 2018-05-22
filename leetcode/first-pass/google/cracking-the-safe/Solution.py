class Solution:
    def extendSeq(self, seq, comb):
        n = len(comb)
        last = seq[-n:]
        for i in range(1, n + 1):
            if last[i:] == comb[:-i]:
                return seq[:-n] + last[:i] + comb
        raise ValueError("unable to extend seq")

    def add_one(self, arr, base):
        rem = 1
        for i in range(len(arr) - 1, -1, -1):
            tmp = arr[i] + rem
            arr[i] = tmp % base
            rem = tmp // base

    def searchNext(self, comb, i, tried, k):
        prefix = comb[i:]
        num = [0] * i
        for _ in range(k ** i):
            self.add_one(num, k)
            next = prefix + ''.join(map(str, num))
            if next not in tried:
                return next
        return None

    def crackSafe(self, n, k):
        tried = set()
        comb = ''.join(['0'] * n)
        tried.add(comb)
        seq = comb
        while True:
            for i in range(1, n + 1):
                next = self.searchNext(comb, i, tried, k)
                if next is not None:
                    break
            if next is None:
                break
            else:
                comb = next
                tried.add(comb)
                seq = self.extendSeq(seq, comb)
        return seq

