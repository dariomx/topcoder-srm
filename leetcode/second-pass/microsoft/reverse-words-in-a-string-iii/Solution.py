class Solution:
    def rev(self, arr, start, end):
        mid = (end - start + 1) // 2
        for i in range(mid):
            arr[start + i], arr[end - i] = arr[end - i], arr[start + i]

    def reverseWords(self, s):
        s = list(s)
        n = len(s)
        start = None
        for i in range(n):
            if s[i] == ' ':
                self.rev(s, start, i - 1)
                start = None
            elif start is None:
                start = i
        if start is not None:
            self.rev(s, start, n - 1)
        return "".join(s)
