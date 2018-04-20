class Solution:
    def countBattleships(self, board):
        res = 0
        for i, row in enumerate(board):
            for j, v in enumerate(row):
                if v == 'X' and not ((i > 0 and board[i - 1][j] == 'X') or (j > 0 and board[i][j - 1] == 'X')):
                    res += 1
        return res
