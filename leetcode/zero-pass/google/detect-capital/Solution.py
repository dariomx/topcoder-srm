class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.upper() == word or \
               word.lower() == word or \
               (word[0] == word[0].upper() and len(word) > 1 and \
                word[1:] == word[1:].lower())
