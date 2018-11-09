class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        i = 0
        cnt = 0
        k = len(flowerbed)
        while i < k:
            if flowerbed[i] == 1:
                i += 2
            elif (i == 0 or flowerbed[i-1] == 0) and \
                (i == k-1 or flowerbed[i+1] == 0):
                cnt += 1
                i += 2
            else:
                i += 1
        return cnt >= n