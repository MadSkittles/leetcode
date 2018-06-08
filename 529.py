class Solution:
    def updateBoard(self, board, click):
        self.row = len(board)
        if not self.row:
            return board
        self.col = len(board[0])
        self.board = board
        self.reveal(*click)
        return self.board

    def reveal(self, x, y):
        if self.board[x][y] == "M":
            self.board[x][y] = "X"
            return
        mine_cnt, next_e = 0, []
        for delta_x, delta_y in [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]:
            if 0 <= x + delta_x < self.row and 0 <= y + delta_y < self.col:
                if self.board[x + delta_x][y + delta_y] == "M":
                    mine_cnt += 1
                elif self.board[x + delta_x][y + delta_y] == "E":
                    next_e.append((x + delta_x, y + delta_y))
        if mine_cnt:
            self.board[x][y] = str(mine_cnt)
        else:
            self.board[x][y] = "B"
            for next_x, next_y in next_e:
                self.reveal(next_x, next_y)
