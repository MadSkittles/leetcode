class Solution:
    def jump(self, nums):
        if len(nums) <= 1:
            return 0
        max_reach = [0]
        index = reach = 0
        while index <= reach < len(nums) - 1:
            if index > max_reach[-1]:
                max_reach.append(reach)
            reach = max(reach, index + nums[index])
            index += 1
        return len(max_reach)


if __name__ == '__main__':
    solution = Solution()
    print(solution.jump([2,1,1,1,4]))
