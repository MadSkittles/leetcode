class Solution:
    def kthGrammar(self, N, K):
        return self.f(N, K - 1)

    def f(self, N, K):
        if N == 1:
            return 0
        parent = self.f(N - 1, K // 2)
        return 1 - K % 2 if parent else K % 2


if __name__ == '__main__':
    solution = Solution()
    for i in range(1, 9):
        print(solution.kthGrammar(30, i))
