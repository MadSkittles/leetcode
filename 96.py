class Solution:
    def numTrees(self, n):
        if n == 0:
            return 0
        self.cache = {}
        return self.f(n)

    def f(self, n):
        if n in self.cache:
            return self.cache[n]

        res = 0
        if n <= 1:
            res = 1
        else:
            for i in range(n):
                res += self.f(i - 0) * self.f(n - 1 - i)

        if n not in self.cache:
            self.cache[n] = res

        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.numTrees(2))
