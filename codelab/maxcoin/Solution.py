class Solution:
    # @param A : list of integers
    # @return an integer
    def maxcoin(self, coin):
        amount = dict()
        n = len(coin)

        #
        def getAmount(i, j):
            print("called with (%d,%d)" % (i,j))
            if (i, j) not in amount:
                if i < 0 or j > (n - 1) or i > j:
                    aij = 0
                elif i == j:
                    aij = coin[i]
                else:
                    maxLeft = coin[j] + \
                        min(getAmount(i+1, j-1), getAmount(i, j-2))
                    maxRight = coin[i] + \
                        min(getAmount(i+1, j-1), getAmount(i+2, j))
                    aij = max(maxLeft, maxRight)
                amount[(i, j)] = aij
            return amount[(i, j)]
        #
        ans = getAmount(0, n - 1)
        print(amount)
        return ans

print(Solution().maxcoin([ 1, 2, 3, 4 ]))
