class Solution:
    def rotatedDigits(self, N):
        rot = {'2': '5', '5': '2', '6': '9', '9': '6',
               '0': '0', '1': '1', '8': '8'}
        ans = 0
        for x in range(1, N + 1):
            y = ""
            for c in str(x):
                if c in rot:
                    y += rot[c]
                else:
                    y = "0"
                    break
            y = int(y)
            if y > 0 and y != x:
                ans += 1
        return ans


