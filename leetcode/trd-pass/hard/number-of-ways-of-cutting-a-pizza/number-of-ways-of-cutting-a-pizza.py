MOD = 10 ** 9 + 7


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        @cache
        def count(x1, y1, x2, y2, cuts):
            if x1 > x2 or y1 > y2:
                return int(cuts == 0)
            elif cuts == 0:
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        if pizza[x][y] == 'A':
                            return 1
                return 0
            else:
                cnt = 0
                for x in range(x1, x2):
                    cnt += count(x1, y1, x, y2, 0) * count(x + 1, y1, x2, y2,
                                                           cuts - 1)
                for y in range(y1, y2):
                    cnt += count(x1, y1, x2, y, 0) * count(x1, y + 1, x2, y2,
                                                           cuts - 1)
                return cnt % MOD

        m, n = len(pizza), len(pizza[0])
        return count(0, 0, m - 1, n - 1, k - 1)
