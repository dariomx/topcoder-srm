class Solution:
    def reverseOnlyLetters(self, S):
        S = list(S)
        start, end = 0, len(S)-1
        while start < end:
            x, y = S[start], S[end]
            xa, ya = x.isalpha(), y.isalpha()
            if xa and ya:
                S[start], S[end] = S[end], S[start]
                end -= 1
                start += 1
            elif xa:
                end -= 1
            elif ya:
                start += 1
            else:
                end -= 1
                start += 1
        return "".join(S)