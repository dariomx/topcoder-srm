class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        map69 = {'6': '9', '9': '6'}

        def duprev(n):
            ret = n
            for d in reversed(n):
                ret += map69.get(d, d)
            return ret

        def add_pairs(ns):
            ret = []
            half = len(ns[0]) // 2
            for n in ns:
                for i in range(half):
                    for d in "0189":
                        ret.append(duprev(n[:(i + 1)] + d + n[(i + 1):half]))
                for d in "18":
                    ret.append(d + n + d)
                for d in "69":
                    ret.append(d + n + map69[d])
            return ret

        def dup_center(ns):
            ret = []
            half = len(ns[0]) // 2
            for n in ns:
                d = n[half]
                if d in map69:
                    center = d + map69[d]
                else:
                    center = d * 2
                ret.append(n[:half] + center + n[half + 1:])
            return ret

        def add_center(ns):
            ret = []
            half = len(ns[0]) // 2
            for n in ns:
                for d in "018":
                    ret.append(n[:half] + d + n[half:])
            return ret

        def f(n):
            if n in cache:
                return cache[n]
            ret = add_pairs(f(n - 2))
            if n % 2 == 0:
                ret += dup_center(f(n - 1))
            else:
                ret += add_center(f(n - 1))
            ret = list({x for x in ret if len(x) == n})
            cache[n] = ret
            return ret

        cache = {1: ['0', '1', '8'], 2: ['11', '88', '69', '96']}
        return f(n)
