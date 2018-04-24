class Solution:
    def PredictTheWinner(self, nums):
        if len(nums) < 2:
            return True
        dp = [[nums[i] if i == j else 0 for j in range(len(nums))] for i in range(len(nums))]
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                dp[i][j] = sum(nums[i:j + 1]) - min(dp[i + 1][j], dp[i][j - 1])
        return dp[0][-1] >= sum(nums) / 2

    def PredictTheWinner1(self, nums):
        self.nums = nums
        self.sum = [0, 0]
        return self.f(0, len(nums) - 1, 0)

    def f(self, start, end, player):
        if start == end:
            self.sum[player] += self.nums[start]
            if self.sum[0] == self.sum[1]:
                res = player == 0
            else:
                res = self.sum[player] > self.sum[1 - player]
            self.sum[player] -= self.nums[start]
            return res

        self.sum[player] += self.nums[start]
        res0 = self.f(start + 1, end, 1 - player)
        self.sum[player] -= self.nums[start]
        res1 = False
        if res0:
            self.sum[player] += self.nums[end]
            res1 = self.f(start, end - 1, 1 - player)
            self.sum[player] -= self.nums[end]
        return not (res0 and res1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.PredictTheWinner([1, 1, 1]))
