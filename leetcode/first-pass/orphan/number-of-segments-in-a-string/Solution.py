class Solution(object):
    def countSegments(self, s):
        ans = 0
        seq = 0
        for x in (s + " "):
            if x == ' ':
                if seq > 0:
                    ans += 1
                seq = 0
            else:
                seq += 1
        return ans