class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        def encodeChar(c):
            return 1 << (ord(c) - ord('a'))
        
        def encodeWord(word):
            enc = 0
            for c in word:
                enc |= encodeChar(c)
            return enc
        
        starts = {encodeWord(w) for w in startWords}
        ans = 0
        for word in targetWords:
            enc = encodeWord(word)
            for c in word:
                cand = enc - encodeChar(c)
                if cand in starts:
                    ans +=1
                    break
        return ans
