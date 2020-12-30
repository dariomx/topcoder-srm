class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        ans = []
        n = len(word)
        def rec(i, abbr):
            if i == n:
                ans.append(abbr)
            else:
                rec(i+1, abbr + word[i])
                if len(abbr) == 0 or abbr[-1].isalpha():
                    for j in range(i, n):
                        rec(j+1, abbr + str(j - i + 1))
        rec(0, '')
        return ans