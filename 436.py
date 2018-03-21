class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def findRightInterval(self, intervals):
        start_map = {}
        for index, interval in enumerate(intervals):
            start_map[interval.start] = min(start_map.get(interval.start, float('inf')), index)
        res, res_map = [], {}
        starts = sorted(start_map.keys())
        ends = sorted(interval.end for interval in intervals)
        i, j = 0, 0
        while j < len(ends):
            if starts[i] >= ends[j]:
                res_map[ends[j]] = start_map[starts[i]]
                j += 1
            elif i < len(starts) - 1:
                i += 1
            else:
                res_map[ends[j]] = -1
                j += 1
        for interval in intervals:
            res.append(res_map[interval.end])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.findRightInterval([Interval(1, 2)]))
    print(solution.findRightInterval([Interval(3, 4), Interval(2, 3), Interval(1, 2)]))
    print(solution.findRightInterval([Interval(1, 4), Interval(2, 3), Interval(3, 4)]))
