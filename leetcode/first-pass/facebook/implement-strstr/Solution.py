class Solution:
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            found = True
            for j in range(len(needle)):
                if needle[j] != haystack[i + j]:
                    found = False
                    break
            if found:
                return i
        return -1

