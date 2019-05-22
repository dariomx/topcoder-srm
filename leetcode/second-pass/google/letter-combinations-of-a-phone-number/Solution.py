class Solution(object):
    def build_combo(self, digits, num, letter):
        combo = ''
        for i in xrange(len(digits)):
            combo += letter[digits[i]][num[i]]
        return combo

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits or '1' in digits:
            return []
        letter = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '
        }
        ans = []
        how_many = 1
        n = len(digits)
        for d in digits:
            how_many *= len(letter[d])
        num = [0] * n
        for i in xrange(how_many):
            ans.append(self.build_combo(digits, num, letter))
            rem = 1
            for j in xrange(n - 1, -1, -1):
                tmp = num[j] + rem
                base = len(letter[digits[j]])
                num[j] = tmp % base
                rem = tmp / base
        return ans
