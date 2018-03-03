class Solution:
    def exist(self, board, word):
        self.row = len(board)
        if self.row <= 0:
            return False
        self.col = len(board[0])
        self.board = board
        self.word = word

        result = False
        for i in range(self.row):
            for j in range(self.col):
                if board[i][j] == word[0]:
                    result = result or self.f(i, j, 0)

        return result

    def f(self, x, y, index):
        if self.board[x][y] != self.word[index]:
            return False
        if index >= len(self.word) - 1:
            return True

        result = False

        for delta_x, delta_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= x + delta_x < self.row and 0 <= y + delta_y < self.col:
                c = self.board[x][y]
                self.board[x][y] = None
                result = result or self.f(x + delta_x, y + delta_y, index + 1)
                self.board[x][y] = c
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], "ABCCED"))
    print(solution.exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], "SEE"))
    print(solution.exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], "ABCB"))
    print(solution.exist([["a"]], "a"))
