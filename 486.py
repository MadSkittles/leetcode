class Solution:
    def PredictTheWinner(self, nums):
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