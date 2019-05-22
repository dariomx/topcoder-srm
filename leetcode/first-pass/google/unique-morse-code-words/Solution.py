class Solution:
    def uniqueMorseRepresentations(self, words):
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        encode = lambda c: morse[ord(c) - ord('a')]
        encs = set()
        for w in words:
            encs.add("".join(map(encode, w)))
        return len(encs)