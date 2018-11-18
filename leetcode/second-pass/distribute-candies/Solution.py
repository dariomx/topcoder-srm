class Solution:
    def distributeCandies(self, candies):
        half = len(candies) // 2
        uniq = set(candies)
        sister = 0
        for i in range(len(uniq)):
            sister += 1
            if sister >= half:
                return i + 1
        return len(uniq)
