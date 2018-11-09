class Solution:
    def sortArrayByParity(self, A):
        even = []
        odd = []
        for x in A:
            if x % 2 == 0:
                even.append(x)
            else:
                odd.append(x)
        return even + odd