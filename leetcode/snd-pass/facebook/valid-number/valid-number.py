class Solution:
    def isSignedInt(self, s, emptyOk=False):
        if len(s) > 0 and s[0] in ('+', '-'):
            s = s[1:]
        if len(s) == 0:
            return emptyOk
        return s.isdigit()

    # None means zero occurrences, -1 means it has more than one
    def uniqIndexOf(self, s, c):
        ix = None
        for i, x in enumerate(s):
            if x == c:
                if ix is None:
                    ix = i
                else:
                    return -1
        return ix

    def isDecPart(self, s):
        return s == '' or s.isdigit()

    def isNumber(self, s: str) -> bool:
        s = s.strip()
        dotIx = self.uniqIndexOf(s, '.')
        expIx = self.uniqIndexOf(s, 'e')
        if (dotIx is not None and dotIx < 0) or (
                expIx is not None and expIx < 0):
            return False
        if dotIx is None and expIx is None:
            return self.isSignedInt(s)
        elif dotIx is None and expIx is not None:
            mant = s[:expIx]
            exp = s[(expIx + 1):]
            return self.isSignedInt(mant) and self.isSignedInt(exp)
        elif dotIx is not None and expIx is None:
            intp = s[:dotIx]
            decp = s[(dotIx + 1):]
            if intp == '' and decp == '':
                return False
            return self.isSignedInt(intp, decp != '') and self.isDecPart(decp)
        else:
            if expIx - dotIx < 1:
                return False
            mant = s[:expIx]
            exp = s[(expIx + 1):]
            intp, decp = mant.split('.')
            return self.isSignedInt(intp, decp != '') and self.isDecPart(
                decp) and \
                   self.isSignedInt(exp)

