class Solution:
    def generateParenthesis(self, n):
        self.result = []
        self.f(1, n, 1, 0, '(')
        return self.result

    def f(self, exist_left, n, left, right, expression):
        if right >= n and left >= n:
            self.result.append(expression)
            return
        if left < n:
            self.f(exist_left + 1, n, left + 1, right, expression + '(')
        if exist_left > 0:
            self.f(exist_left - 1, n, left, right + 1, expression + ')')


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(3))
