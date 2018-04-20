class Solution:
    def countBattleships(self, board):
        return sum(v == 'X' and not ((i > 0 and board[i - 1][j] == 'X') or (j > 0 and board[i][j - 1] == 'X')) for i, row in enumerate(board) for j, v in enumerate(row))
