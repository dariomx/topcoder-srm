# single pass was possible using the max(zeros - ones) trick, #fail again

class Solution:
    def maxScore(self, s: str) -> int:
        ones = sum(map(int, s))
        zeros = 0
        ans = 0
        for i in range(len(s)-1):
            bit = s[i]
            if bit == '1':
                ones -= 1
            else:
                zeros += 1
            ans = max(ans, zeros + ones)
        return ans