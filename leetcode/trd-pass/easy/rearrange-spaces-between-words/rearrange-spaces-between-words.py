class Solution:
    def getWordsSpc(self, text):
        words, spc = [], -1
        w = ''
        for c in (text + ' '):
            if c == ' ':
                spc += 1
                if w != '':
                    words.append(w)
                w = ''
            else:
                w += c
        return words, spc

    def reorderSpaces(self, text: str) -> str:
        words, spc = self.getWordsSpc(text)
        if len(words) == 1:
            return words[0] + (' ' * spc)
        else:
            q, r = divmod(spc, len(words) - 1)
            sep = ' ' * q
            rem = ' ' * r
            return sep.join(words) + rem
