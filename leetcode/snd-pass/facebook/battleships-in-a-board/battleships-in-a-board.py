class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        n, m = len(board), len(board[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                left_empty = (j == 0 or board[i][j - 1] == '.')
                up_empty = (i == 0 or board[i - 1][j] == '.')
                if left_empty and up_empty and board[i][j] == 'X':
                    ans += 1
        return ans
