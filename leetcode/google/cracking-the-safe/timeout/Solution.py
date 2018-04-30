class Solution:
    def add_one(self, arr, base):
        rem = 1
        for i in range(len(arr)-1, -1, -1):
            tmp = arr[i] + rem
            arr[i] = tmp % base
            rem = tmp // base

    def explore(self, start, n, k):
        string = start
        used = set([start])
        pend = set()
        total = k**n
        while len(used) < total:
            found = False
            last = string[-n:]
            for i in range(1, n+1):
                base = last[i:]
                num = [0] * i
                for _ in range(k**i):
                    cand = base + ''.join(map(str, num))
                    if cand not in used:
                        if not found:
                            found = True
                            string += cand[-i:]
                            used.add(cand)
                        elif cand not in pend:
                            pend.add(cand)
                    self.add_one(num, k)
                if found:
                    break
            if not found and pend:
                cand = pend.pop()
                if cand not in used:
                    string += cand
        return string

    def crackSafe(self, n, k):
        min_str = None
        num = [0] * n
        for _ in range(k**n):
            start = ''.join(map(str, num))
            string = self.explore(start, n, k)
            if min_str is None or len(string) < len(min_str):
                min_str = string
        return min_str
#
print(Solution().crackSafe(2, 2))