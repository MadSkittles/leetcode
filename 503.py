class Solution:
    def nextGreaterElements(self, nums):
        stack, res = [], [-1] * len(nums)
        for i in range(2 * len(nums)):
            n = nums[i % len(nums)]
            while stack and n > stack[-1][0]:
                res[stack.pop()[1]] = n
            stack.append((n, i % len(nums)))
        return res

    def nextGreaterElements1(self, nums):
        long_nums = nums * 2
        res = [float('inf')] * len(long_nums)
        for i in range(len(long_nums) - 2, -1, -1):
            j = i + 1
            while j != float('inf') and long_nums[j] <= long_nums[i]:
                j = res[j]
            res[i] = j
        return [long_nums[r] if r != float('inf') else -1 for r in res[:len(nums)]]


if __name__ == '__main__':
    solution = Solution()
    print(solution.nextGreaterElements([1, 2, 1]))
