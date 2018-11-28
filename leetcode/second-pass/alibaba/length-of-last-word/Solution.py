class Solution:
    def lengthOfLastWord(self, s):
        ans = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                if ans > 0:
                    break
            else:
                ans += 1
        return ans
