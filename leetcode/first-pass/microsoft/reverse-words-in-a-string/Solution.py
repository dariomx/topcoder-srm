class Solution(object):
    def shift_trim(self, arr):
        i = 0
        n = len(arr)
        for j in range(n):
            if arr[j] == ' ':
                if i > 0 and arr[i - 1] != ' ':
                    arr[i] = ' '
                    i += 1
            else:
                arr[i] = arr[j]
                if i != j:
                    arr[j] = ' '
                i += 1
        while arr and arr[-1] == ' ':
            arr.pop()

    def rev(self, arr, start, end):
        size = end - start + 1
        for i in range(size // 2 + size % 2):
            arr[start + i], arr[end - i] = arr[end - i], arr[start + i]

    def reverseWords(self, s):
        s = list(s)
        self.shift_trim(s)
        n = len(s)
        self.rev(s, 0, n - 1)
        start, end = 0, 0
        s.append(' ')
        for i in range(n + 1):
            if s[i] == ' ':
                self.rev(s, start, end)
                start, end = i + 1, i + 1
            else:
                end = i
        s.pop()
        return ''.join(s)
