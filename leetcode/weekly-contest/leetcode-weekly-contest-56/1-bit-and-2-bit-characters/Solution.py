class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        one_bit = False
        i = 0
        while i < len(bits):
            bit = bits[i]
            if bit == 1:
                one_bit = False
                i += 1
            else:
                one_bit = True
            i += 1
        return one_bit
