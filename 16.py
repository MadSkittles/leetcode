class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        min_diff = None
        result = None
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if not min_diff or abs(s - target) < min_diff:
                    min_diff = abs(s - target)
                    result = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return target
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSumClosest([-1, 2, 1, -4],1))
