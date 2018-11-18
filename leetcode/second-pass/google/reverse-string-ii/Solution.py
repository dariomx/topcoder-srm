class Solution:
    def reverseStr(self, s, k):
        n = len(s)
        s = list(s)
        start, end = 0, min(k-1, n-1)
        while start < end:
            i, j = start, end
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            start, end = start+2*k, min(end+2*k, n-1)
        return "".join(s)