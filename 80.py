class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 0:
            return 0
        cur_val, cur_cnt, index = nums[0], 1, 1
        while index < len(nums):
            if nums[index] == cur_val:
                cur_cnt += 1
                if cur_cnt > 2:
                    del nums[index]
                    index -= 1
            else:
                cur_val, cur_cnt = nums[index], 1
            index += 1
        return len(nums)


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates([1, 2, 2, 2]))
    print(solution.removeDuplicates([]))
