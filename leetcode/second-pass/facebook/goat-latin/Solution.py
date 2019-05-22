class Solution:
    def toGoatLatin(self, S):
        gl = ""
        words = S.split()
        for i in range(len(words)):
            w = words[i]
            if w[0].lower() in ('a','e','i','o','u'):
                gl += w
            else:
                gl += w[1:] + w[0]
            gl += "ma" + ('a' * (i+1)) + " "
        return gl.strip()