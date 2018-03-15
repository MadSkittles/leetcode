class Solution:
    def lexicalOrder(self, n):
        self.n = n
        self.res = []
        for i in range(1, 10):
            self.f(i)
        return self.res

    def f(self, base):
        if base > self.n:
            return
        self.res.append(base)
        for i in range(0, 10):
            self.f(base * 10 + i)


if __name__ == '__main__':
    solution = Solution()
    print(solution.lexicalOrder(13))
