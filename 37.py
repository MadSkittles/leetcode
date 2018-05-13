class Solution:
    def solveSudoku(self, board):
        self.pos, self.board = [], board
        self.row, self.col, self.block = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    self.pos.append((i, j))
                else:
                    self.row[i].add(board[i][j])
                    self.col[j].add(board[i][j])
                    self.block[(i // 3) * 3 + (j // 3)].add(board[i][j])
        self.f(0)

    def f(self, index):
        if index >= len(self.pos):
            return True
        i, j = self.pos[index]
        candidates = {'1', '2', '3', '4', '5', '6', '7', '8', '9'} - self.row[i] - self.col[j] - self.block[(i // 3) * 3 + (j // 3)]
        if not candidates:
            return False
        for n in candidates:
            self.row[i].add(n)
            self.col[j].add(n)
            self.block[(i // 3) * 3 + (j // 3)].add(n)
            self.board[i][j] = n
            if self.f(index + 1):
                return True
            self.row[i].discard(n)
            self.col[j].discard(n)
            self.block[(i // 3) * 3 + (j // 3)].discard(n)


if __name__ == '__main__':
    solution = Solution()
    sudoku = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."],
              ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
              [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    solution.solveSudoku(sudoku)
    for row in sudoku:
        print(' '.join(row))
