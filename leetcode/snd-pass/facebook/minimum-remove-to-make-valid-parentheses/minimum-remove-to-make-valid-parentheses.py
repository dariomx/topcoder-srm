class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_s, close_s = [], []
        for i, c in enumerate(s):
            if c == '(':
                open_s.append(i)
            elif c == ')':
                if open_s:
                    open_s.pop()
                else:
                    close_s.append(i)
        open_s, close_s = set(open_s), set(close_s)
        return ''.join([s[i] for i in range(len(s)) \
                        if i not in open_s and i not in close_s])
