class Solution:
    def solveNQueens(self, n):
        self.res, self.flag = [], [True] * n
        self.f(0, (), n)
        result = []
        for queens in self.res:
            l = []
            for p in queens:
                l.append('.' * p + 'Q' + '.' * (n - 1 - p))
            result.append(l)
        return result

    def f(self, index, queens, n):
        if index >= n:
            self.res.append(queens)
        for pos in range(n):
            if self.flag[pos] and not any(abs(pos - queens[i]) == index - i for i in range(index)):
                self.flag[pos] = False
                self.f(index + 1, queens + (pos,), n)
                self.flag[pos] = True


if __name__ == '__main__':
    solution = Solution()
    print(solution.solveNQueens(5))
