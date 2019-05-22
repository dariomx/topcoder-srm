class Solution:
    def compress_star(self, p):
        new_p = ""
        for c in p:
            if not (c == "*" and new_p and new_p[-1] == '*'):
                new_p += c
        return new_p

    def isMatch(self, s, p):
        p = self.compress_star(p)
        n = len(s)
        m = len(p)
        cache = dict()

        def rec(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            ret = False
            if i == n and j == m:
                ret = True
            elif (i == n and j < m):
                if j == m - 1 and p[j] == '*':
                    ret = True
            elif (i < n and j == m):
                None
            elif s[i] == p[j] or p[j] == '?':
                ret = rec(i + 1, j + 1)
            elif p[j] == "*":
                # star matches zero or first one
                # got idea from
                # https://www.quora.com/What-is-the-best-way-to-implement
                # -Kleene-star-closure-operation-in-C-or-C++
                # before this trick, i was putting into the stack all possible
                # options for i; which lead to a lot of redundant work.
                ret = rec(i, j + 1) or rec(i + 1, j)
            cache[(i, j)] = ret
            return ret

        return rec(0, 0)

