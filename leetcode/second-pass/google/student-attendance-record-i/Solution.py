class Solution:
    def checkRecord(self, s):
        cnt = {'A': 0, 'L': 0}
        prev = None
        for a in s:
            if a == 'L' and a != prev:
                cnt[a] = 0
            if a != 'P':
                cnt[a] += 1
            if a == 'A' and cnt[a] > 1:
                return False
            elif a == 'L' and cnt[a] > 2:
                return False
            prev = a
        return True

