class Solution:
    def combine(self, n, k):
        self.result = []
        self.n = n
        self.f(k, ())
        return self.result

    def f(self, left, comb):
        if left <= 0:
            self.result.append(comb)
            return

        for i in range(comb[-1] + 1 if len(comb) > 0 else 1, self.n + 1):
            self.f(left - 1, (*comb, i))


if __name__ == '__main__':
    solution = Solution()
    print(solution.combine(4, 2))
