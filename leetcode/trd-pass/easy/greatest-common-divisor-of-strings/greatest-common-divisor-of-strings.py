class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) == 0:
            return str2
        elif len(str2) == 0:
            return str1
        else:
            if str1 > str2:
                str1, str2 = str2, str1
            ix = str2.find(str1)
            # TODO: why assuming prefix is fine?
            if ix != 0:
                return ''
            else:
                return self.gcdOfStrings(str2[len(str1):], str1)

