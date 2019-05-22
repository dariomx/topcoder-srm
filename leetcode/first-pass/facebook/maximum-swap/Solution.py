class Solution:
    def maximumSwap(self, num):
        num = list(map(int, str(num)))
        n = len(num)
        max_dig = [0] * n
        max_pos = [0] * n
        max_dig[n - 1] = num[n - 1]
        max_pos[n - 1] = n - 1
        for i in range(n - 2, -1, -1):
            if num[i] <= max_dig[i + 1]:
                max_dig[i] = max_dig[i + 1]
                max_pos[i] = max_pos[i + 1]
            else:
                max_dig[i] = num[i]
                max_pos[i] = i
        for i in range(n - 1):
            if num[i] < max_dig[i + 1]:
                j = max_pos[i + 1]
                num[i], num[j] = num[j], num[i]
                break
        return int(''.join(map(str, num)))
