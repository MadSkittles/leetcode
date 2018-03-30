class Solution:
    def findMinDifference(self, timePoints):
        timePoints = sorted(map(lambda x: [int(n) for n in x.split(':')], timePoints))
        timePoints.append([timePoints[0][0] + 24, timePoints[0][1]])
        res = float('inf')
        for i in range(1, len(timePoints)):
            diff = (timePoints[i][0] - timePoints[i - 1][0]) * 60 + (timePoints[i][1] - timePoints[i - 1][1])
            if diff > 720:
                diff = 1440 - diff
            res = min(res, diff)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMinDifference(["23:59", "00:00"]))
