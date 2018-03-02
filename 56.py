class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '[%d,%d]' % (self.start, self.end)

    __repr__ = __str__

    @classmethod
    def build(cls, l):
        result = []
        for i in l:
            result.append(cls(i[0], i[1]))
        return result


class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda interval: interval.start)
        result = []
        for i in range(0, len(intervals)):
            if not result or result[-1].end < intervals[i].start:
                result.append(intervals[i])
            else:
                n = result.pop()
                result.append(Interval(n.start, max(n.end, intervals[i].end)))
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.merge(Interval.build([[1, 3], [2, 6], [8, 10], [15, 18]])))
