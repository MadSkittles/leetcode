class Solution:
    def totalNQueens(self, n):
        self.res, self.flag = 0, [True] * n
        self.f(0, (), n)
        return self.res

    def f(self, index, queens, n):
        if index >= n:
            self.res += 1
        for pos in range(n):
            if self.flag[pos] and not any(abs(pos - queens[i]) == index - i for i in range(index)):
                self.flag[pos] = False
                self.f(index + 1, queens + (pos,), n)
                self.flag[pos] = True


if __name__ == '__main__':
    solution = Solution()
    print(solution.totalNQueens(5))
