class Solution:
    def countBattleships(self, board):
        single_ship, horizontal_ship, vertical_ship = 0, 0, 0
        for i in range(len(board)):
            j, cnt = 0, 0
            while j < len(board[0]):
                if board[i][j] == 'X':
                    cnt += 1
                else:
                    if cnt > 1:
                        horizontal_ship += 1
                    cnt = 0
                j += 1
            if cnt > 1:
                horizontal_ship += 1

        if len(board) > 1:
            for j in range(len(board[0])):
                i, cnt = 0, 0
                while i < len(board):
                    if board[i][j] == 'X':
                        cnt += 1
                    else:
                        if cnt > 1:
                            vertical_ship += 1
                        cnt = 0
                    i += 1
                if cnt > 1:
                    vertical_ship += 1

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    result = True
                    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        if 0 <= i + di < len(board) and 0 <= j + dj < len(board[0]) and board[i + di][j + dj] == 'X':
                            result = False
                    if result:
                        single_ship += 1

        return single_ship + horizontal_ship + vertical_ship


if __name__ == '__main__':
    solution = Solution()
    print(solution.countBattleships(['X..X',
                                     'XX.X',
                                     '...X']))
