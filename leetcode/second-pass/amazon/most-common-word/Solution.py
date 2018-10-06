from collections import defaultdict


class Solution:
    def mostCommonWord(self, paragraph, banned):
        banned = set(banned)
        cnt = defaultdict(lambda: 0)
        maxCnt = 0
        maxTxt = ""

        def procWord(w, txt):
            nonlocal maxCnt, maxTxt
            if w not in banned:
                cnt[w] += 1
                if cnt[w] > maxCnt:
                    maxCnt = cnt[w]
                    maxTxt = txt

        txt = ""
        word = ""
        for c in paragraph:
            c = c.lower()
            if c != " ":
                txt += c
                if c.isalpha():
                    word += c
            elif word:
                procWord(word, txt)
                txt = ""
                word = ""
        procWord(word, txt)
        if not maxTxt[-1].isalpha():
            maxTxt = maxTxt[:-1]
        return maxTxt
