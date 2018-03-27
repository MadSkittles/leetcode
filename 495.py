class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        res = start = end = 0
        for time in timeSeries:
            if time >= end:
                res += end - start
                start, end = time, time + duration
            else:
                end = max(end, time + duration)
        res += end - start
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.findPoisonedDuration([1, 4], 2))
