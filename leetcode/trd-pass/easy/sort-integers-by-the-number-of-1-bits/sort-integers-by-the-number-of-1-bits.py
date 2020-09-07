class Solution:
    def cntBits(self, x):
        mask = 1
        cnt = 0
        for i in range(16):
            cnt += (x & mask) >> i
            mask <<= 1
        return cnt

    def sortByBits(self, arr: List[int]) -> List[int]:
        cnt = {x: self.cntBits(x) for x in arr}
        arr.sort(key=lambda x: (cnt[x], x))
        return arr
