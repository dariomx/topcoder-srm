from collections import Counter


class Solution:
    def is_valid(self, a, b):
        if b <= 0.5 * a + 7:
            return False
        if b > a:
            return False
        if b > 100 and a < 100:
            return False
        return True

    def numFriendRequests(self, ages):
        freq = Counter(ages)
        ages = sorted(freq.keys(), reverse=True)
        n = len(ages)
        req = 0
        for i in range(n):
            a = ages[i]
            if self.is_valid(a, a):
                req += freq[a] ** 2 - freq[a]
            for j in range(i + 1, n):
                b = ages[j]
                if self.is_valid(a, b):
                    req += freq[a] * freq[b]
        return req
