class Solution:
    def nextPermutation(self, nums):
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                break
        else:
            return self.reverse(nums)

        point = i
        for i in range(len(nums) - 1, point - 1, -1):
            if nums[point - 1] < nums[i]:
                self.insert(nums, i, point - 1)
                return

    def reverse(self, nums, start=None, end=None):
        start, end = start or 0, end or len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def insert(self, nums, pos, insert_pos):
        nums[pos], nums[insert_pos] = nums[insert_pos], nums[pos]
        self.reverse(nums, insert_pos + 1)


if __name__ == '__main__':
    from itertools import permutations

    solution = Solution()
    p = list(permutations([1, 2, 3, 4, 5]))
    for i in range(len(p)):
        d = list(p[i]).copy()
        solution.nextPermutation(d)
        print(p[(i + 1) % len(p)], d)
