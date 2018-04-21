class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        tower = [[poured]]
        for i in range(1, query_row + 1):
            next_floor = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    next_floor.append((tower[i - 1][0 if j == 0 else i - 1] - 1) / 2 if tower[i - 1][0 if j == 0 else i - 1] > 1 else 0)
                else:
                    next_floor.append(((tower[i - 1][j - 1] - 1) / 2 if tower[i - 1][j - 1] > 1 else 0) + ((tower[i - 1][j] - 1) / 2 if tower[i - 1][j] > 1 else 0))
            tower.append(next_floor)
        return tower[query_row][query_glass] if tower[query_row][query_glass] <= 1 else 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.champagneTower(1, 1, 1))
    print(solution.champagneTower(2, 1, 1))
