class Solution:
    def isValidSudoku(self, board):
        block_set = [set() for _ in range(9)]
        for i in range(9):
            row = set()
            col = set()
            for j in range(9):
                if board[i][j] != '.':
                    if '1' <= board[i][j] <= '9':
                        if board[i][j] in row:
                            return False
                        else:
                            row.add(board[i][j])

                        if board[i][j] in block_set[int(i / 3) * 3 + int(j / 3)]:
                            return False
                        else:
                            block_set[int(i / 3) * 3 + int(j / 3)].add(board[i][j])
                    else:
                        return False
                if board[j][i] != '.':
                    if '1' <= board[j][i] <= '9':
                        if board[j][i] in col:
                            return False
                        else:
                            col.add(board[j][i])
                    else:
                        return False

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValidSudoku(
        [[".", "8", "7", "6", "5", "4", "3", "2", "1"], ["2", ".", ".", ".", ".", ".", ".", ".", "."],
         ["3", ".", ".", ".", ".", ".", ".", ".", "."], ["4", ".", ".", ".", ".", ".", ".", ".", "."],
         ["5", ".", ".", ".", ".", ".", ".", ".", "."], ["6", ".", ".", ".", ".", ".", ".", ".", "."],
         ["7", ".", ".", ".", ".", ".", ".", ".", "."], ["8", ".", ".", ".", ".", ".", ".", ".", "."],
         ["9", ".", ".", ".", ".", ".", ".", ".", "."]]))
