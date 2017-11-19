class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        cnt = 1
        for node in preorder.split(','):
            if cnt == 0:
                return False
            elif node == '#':
                cnt -= 1
            else:
                cnt += 1
        return cnt == 0
