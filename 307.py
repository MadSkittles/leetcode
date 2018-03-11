class NumArray:

    def __init__(self, nums):
        self.sum_list = []
        self.nums = nums
        self.diff = [0] * len(nums)
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            self.sum_list.append(sum)

    def update(self, i, val):
        self.diff[i] = val - self.nums[i]

    def sumRange(self, i, j):
        return self.sum_list[j] - (self.sum_list[i - 1] if i > 0 else 0) + sum(self.diff[i:j + 1])


obj = NumArray([1, 3, 5])
print(obj.sumRange(0, 2))
obj.update(1, 2)
print(obj.sumRange(0, 2))
