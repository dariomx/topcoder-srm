from collections import Counter


class Solution:
    def canConstruct(self, ransomNote, magazine):
        cnt = Counter(magazine)
        for c in ransomNote:
            if cnt[c] > 0:
                cnt[c] -= 1
            else:
                return False
        return True
