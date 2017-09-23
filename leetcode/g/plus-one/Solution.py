class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        rem = 1
        for i in xrange(len(digits) - 1, -1, -1):
            tmp = rem + digits[i]
            digits[i] = tmp % 10
            rem = tmp / 10
        if rem > 0:
            digits = [rem] + digits
        return digits
