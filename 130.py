class Solution:
    def solve(self, board):
        row = len(board)
        if not row:
            return
        col = len(board[0])
        visited = set()
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O' and (i, j) not in visited:
                    visited.add((i, j))
                    cur_visited, q, flag = {(i, j)}, [(i, j)], True
                    while q:
                        next_q = []
                        for x, y in q:
                            for delta_x, delta_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                if 0 <= x + delta_x < row and 0 <= y + delta_y < col:
                                    if (x + delta_x, y + delta_y) not in cur_visited and board[x + delta_x][y + delta_y] == 'O':
                                        cur_visited.add((x + delta_x, y + delta_y))
                                        next_q.append((x + delta_x, y + delta_y))
                                else :
                                    flag = False
                        q = next_q
                    visited.update(cur_visited)
                    if flag:
                        for x, y in cur_visited:
                            board[x][y] = 'X'


if __name__ == '__main__':
    solution = Solution()
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    solution.solve(board)
    print(board)
