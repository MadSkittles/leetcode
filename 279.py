class Solution:
    def numSquares(self, n):
        dp = [0]
        while len(dp) <= n:
            dp.append(min(dp[-i ** 2] for i in range(1, int(len(dp) ** 0.5 + 1))) + 1)
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.numSquares(6255))
