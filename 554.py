class Solution:
    def leastBricks(self, wall):
        from collections import Counter
        from itertools import accumulate
        c = Counter()
        for w in wall:
            c.update(accumulate(w[:-1]))
        return len(wall) - max(c.values(), default=0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.leastBricks([[1], [1], [1]]))
