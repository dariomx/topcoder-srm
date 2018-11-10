class Solution:
    def rotateString(self, A, B):
        n = len(A)
        if len(B) != n:
            return False
        elif A == B:
            return True
        for i in range(1, n+1):
            found = True
            for j in range(n):
                if A[(j+i) % n] != B[j]:
                    found = False
                    break
            if found:
                return True
        return False