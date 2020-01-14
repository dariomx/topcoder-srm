class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        n = len(words)
        try:
            for i in xrange(n):
                for j in xrange(len(words[i])):
                    if words[i][j] != words[j][i]:
                        return False
        except IndexError:
            return False
        return True
