class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        word = ''
        index = 0
        for c in sentence + ' ':
            if c == ' ':
                index += 1
                if word.startswith(searchWord):
                    return index
                word = ''
            else:
                word += c
        return -1