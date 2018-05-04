class Solution:
    def calculateMinimumHP(self, dungeon):
        if not dungeon:
            return 1
        dp = [[1] * len(dungeon[0]) for _ in dungeon]
        for i in range(len(dungeon) - 1, -1, -1):
            for j in range(len(dungeon[0]) - 1, -1, -1):
                l = []
                if i < len(dungeon) - 1:
                    l.append(dp[i + 1][j] - dungeon[i][j])
                if j < len(dungeon[0]) - 1:
                    l.append(dp[i][j + 1] - dungeon[i][j])
                dp[i][j] = max(1 - dungeon[i][j], 1, min(l, default=float('-inf')))
        return dp[0][0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
