import random


class Solution:
    def __init__(self, n_rows, n_cols):
        self.rows = n_rows
        self.cols = n_cols
        self.size = self.rows * self.cols
        self.matrix = set()

    def flip(self):
        n = random.randint(0, self.size - 1)
        while n in self.matrix:
            n = random.randint(0, self.size - 1)
        row, col = n // self.cols, n % self.cols
        self.matrix.add(n)
        return row, col

    def reset(self):
        self.matrix = set()


if __name__ == "__main__":
    solution = Solution(2, 3)
    print(solution.flip())
    print(solution.flip())
    print(solution.flip())
    print(solution.flip())
