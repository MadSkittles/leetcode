class Solution(object):
    def find132pattern(self, nums):
        if len(nums) < 3:
            return False

        stack = [[nums[0], nums[0]]]
        minimum = nums[0]
        for num in nums[1:]:
            if num <= minimum:
                minimum = num
            else:
                while stack and num > stack[-1][0]:
                    if num < stack[-1][1]:
                        return True
                    else:
                        stack.pop()
                stack.append([minimum, num])

        return False