class Solution:
    def minimumTotal(self, triangle):
        from functools import reduce
        return reduce(lambda x, y: [min(x[i], x[i + 1]) + y[i] for i in range(len(y))], triangle[::-1])[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]))
