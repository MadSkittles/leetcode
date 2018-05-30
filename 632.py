class Solution:
    def smallestRange(self, nums):
        from queue import PriorityQueue
        q, max_, res = PriorityQueue(), float('-inf'), [float('-inf'), float('inf')]
        for index, n in enumerate(nums):
            q.put((n[0], index, 0))
            max_ = max(max_, n[0])
        while True:
            num, index, p = q.get()
            if max_ - num < res[1] - res[0]:
                res = [num, max_]
            p += 1
            if p >= len(nums[index]):
                break
            max_ = max(max_, nums[index][p])
            q.put((nums[index][p], index, p))
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]))
