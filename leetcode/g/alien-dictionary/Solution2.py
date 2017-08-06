from math import copysign

class Solution(object):
    def calc_closure(self, chars, less_than):
        lt_closure = set()
        for start in chars:
            stack = [(start, [])]
            visited = set()
            while stack:
                c, path = stack.pop()
                if c in visited:
                    continue
                visited.add(c)
                for lt_c in path:
                    lt_closure.add((lt_c, c))
                for (x, y) in less_than:
                    if x == c:
                        stack.append((y, path + [c]))
        return lt_closure

    def calc_alien_lt(self, words, cmp_chars):
        n = len(words)
        max_len = max(map(len, words))
        less_than = set()
        for k in xrange(1, max_len + 1):
            for j in xrange(n - 1, 0, -1):
                w1 = words[j - 1]
                w2 = words[j]
                if len(w1) >= k and len(w2) >= k:
                    c1, c2 = w1[k-1], w2[k-1]
                    if w1[:k] == w2[:k] and c1 != c2:
                        if (c2, c1) in less_than:
                            raise KeyError((c1, c2))
                        less_than.add((c1, c2))
                        cmp_chars.add(c1)
                        cmp_chars.add(c2)
        return less_than

    def calc_alien_cmp(self, words, chars, cmp_chars):
        less_than = self.calc_alien_lt(words, cmp_chars)
        less_than = less_than.union(self.calc_closure(chars, less_than))
        def alien_cmp(x,y):
            if x == y:
                return 0
            else:
                if (x,y) in less_than:
                    return -1
                elif (y,x) in less_than:
                    return 1
                else:
                    return int(copysign(1, ord(x) - ord(y)))
        return alien_cmp

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        chars = set()
        for w in words:
            chars = chars.union(set(w))
        try:
            cmp_chars = set()
            alien_cmp = self.calc_alien_cmp(words, chars, cmp_chars)
            nocmp_chars = list(chars - cmp_chars)
            cmp_chars = list(cmp_chars)
            cmp_chars.sort(cmp=alien_cmp)
            sorted_chars = nocmp_chars + cmp_chars
            return ''.join(sorted_chars)
        except KeyError, e:
            print(e)
            return ''

words = ["wrt","wrf","er","ett","rftt"]
#words = ["z", "x", "z"]
#words = ["zy", "zx"]
words = ["ac","ab","b"]
words = ["za","zb","ca","cb"]
print(Solution().alienOrder(words))
