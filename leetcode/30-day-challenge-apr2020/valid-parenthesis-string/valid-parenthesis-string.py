class Solution:
    def backtrack(self, i, s, cnt):
        if i == len(s):
            if cnt == 0:
                raise ValueError()
            else:
                return
        key = (i, cnt)
        if key in self.cache:
            return
        self.cache.add(key)
        if s[i] == '(':
            self.backtrack(i + 1, s, cnt + 1)
        elif s[i] == ')':
            if cnt > 0:
                self.backtrack(i + 1, s, cnt - 1)
        else:
            self.backtrack(i + 1, s, cnt + 1)
            if cnt > 0:
                self.backtrack(i + 1, s, cnt - 1)
            self.backtrack(i + 1, s, cnt)

    def checkValidString(self, s: str) -> bool:
        self.cache = set()
        try:
            self.backtrack(0, s, 0)
        except ValueError:
            return True
        return False