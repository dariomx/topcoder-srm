class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        k = 10
        mine = [0] * k
        his = [0] * k
        bulls, cows = 0, 0
        for i in range(len(secret)):
            s, g = int(secret[i]), int(guess[i])
            if s == g:
                bulls += 1
            else:
                mine[s] += 1
                his[g] += 1
        for i in range(k):
            cows += min(mine[i], his[i])
        return "%dA%dB" % (bulls, cows)
