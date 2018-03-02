class Solution:
    def canJump(self, nums):
        if not nums:
            return False
        cur_pos = 0
        while nums[cur_pos] > 0:
            max_reach = cur_pos + nums[cur_pos]
            max_next = max_reach
            for step in range(1, nums[cur_pos] + 1):
                next = cur_pos + step
                if next >= (len(nums) - 1):
                    return True
                if next + nums[next] >= max_reach:
                    max_reach = next + nums[next]
                    max_next = next
            cur_pos = max_next

        return cur_pos >= (len(nums) - 1)


if __name__ == '__main__':
    # import yaml
    #
    # with open('data/55.yml', 'r') as f:
    #     case = yaml.load(f)
    # print('start')
    solution = Solution()
    # print(solution.canJump(case['case1']))

    print(solution.canJump([1,1,2,2,0,1,1]))
