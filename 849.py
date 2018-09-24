class Solution:
    def maxDistToClosest(self, seats):
        res, pre = float('-inf'), None
        for i, n in enumerate(seats):
            if n == 1:
                if pre is None:
                    res = max(res, i)
                else:
                    res = max(res, (i - pre) // 2)
                pre = i
        res = max(res, len(seats) - pre - 1)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxDistToClosest([1, 0]))
