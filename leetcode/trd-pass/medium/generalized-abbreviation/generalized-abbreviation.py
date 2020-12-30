class Solution:
    def parseNum(self, s):
        num = 0
        i = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        return num, i

    def generateAbbreviations(self, word: str) -> List[str]:
        if len(word) == 0:
            ret = []
        elif len(word) == 1:
            ret = [word, '1']
        else:
            ret = []
            for abbr in self.generateAbbreviations(word[1:]):
                ret.append(word[0] + abbr)
                if abbr[0].isdigit():
                    cnt, i = self.parseNum(abbr)
                    ret.append(str(cnt + 1) + abbr[i:])
                else:
                    ret.append('1' + abbr)
        return ret
