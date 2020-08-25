class Solution:
    def dedup(self, s):
        newS = []
        for c in s:
            if newS and c == newS[-1]:
                newS.pop()
            else:
                newS.append(c)
        return ''.join(newS)

    def removeDuplicates(self, S: str) -> str:
        while True:
            newS = self.dedup(S)
            if newS == S:
                break
            else:
                S = newS
        return S
