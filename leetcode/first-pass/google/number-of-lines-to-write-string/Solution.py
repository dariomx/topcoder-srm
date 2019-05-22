class Solution:
    def numberOfLines(self, widths, S):
        ans = [0, 0]
        line = 0
        for c in S:
            i = ord(c) - ord('a')
            w = widths[i]
            if line + w > 100:
                ans[0] += 1
                line = 0
            line += w
        if line > 0:
            ans[0] += 1
            ans[1] = line
        return ans
