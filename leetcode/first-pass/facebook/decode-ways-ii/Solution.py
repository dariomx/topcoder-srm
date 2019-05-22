mod_ans = int(1e9 + 7)


class Solution:
    def decode1(self, x):
        if x == '0':
            return 0
        elif x == '*':
            return 9
        else:
            return 1

    def decode2(self, x, y):
        if x == '*' and y == '*':
            return 15
        elif x == '*' and y != '*':
            if y == '0':
                return 2
            elif '1' <= y <= '6':
                return 2
            else:
                return 1
        elif x != '*' and y == '*':
            if x == '1':
                return 9
            elif x == '2':
                return 6
            else:
                return 0
        else:
            dx = ord(x) - ord('0')
            dy = ord(y) - ord('0')
            if 10 <= dx * 10 + dy <= 26:
                return 1
            else:
                return 0

    def numDecodings(self, s):
        n = len(s)
        rec = [0] * (n + 1)
        rec[n] = 1
        rec[n - 1] = self.decode1(s[n - 1])
        for i in range(n - 2, -1, -1):
            rec[i] = self.decode1(s[i]) * rec[i + 1]
            if i < n - 1:
                rec[i] += self.decode2(s[i], s[i + 1]) * rec[i + 2]
        return rec[0] % mod_ans
