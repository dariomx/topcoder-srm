class Solution:
    def reformat(self, s: str) -> str:
        def join(A, B):
            return ''.join(a + b for a, b in zip(A, B))

        alpha = []
        digits = []
        for c in s:
            if c.isalpha():
                alpha.append(c)
            else:
                digits.append(c)
        if abs(len(alpha) - len(digits)) > 1:
            return ''
        elif len(alpha) > len(digits):
            return join(alpha, digits) + alpha[-1]
        elif len(digits) > len(alpha):
            return join(digits, alpha) + digits[-1]
        else:
            return join(digits, alpha)
