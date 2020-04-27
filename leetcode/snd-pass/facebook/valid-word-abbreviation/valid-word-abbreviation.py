class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, n = 0, len(word)
        j, m = 0, len(abbr)
        while i < n and j < m:
            if abbr[j] == '0' and (j == 0 or not abbr[j-1].isdigit()):
                return False
            skip = 0
            while j < m and abbr[j].isdigit():
                skip = skip*10 + int(abbr[j])
                j += 1
            if skip > 0:
                i += skip
            else:
                if word[i] == abbr[j]:
                    i += 1
                    j += 1
                else:
                    return False
        return i == n and j == m