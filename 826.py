class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        import bisect
        s = sorted(zip(difficulty, profit))
        res, difficulty, max_profit, profit = 0, [], float('-inf'), []
        for d, p in s:
            max_profit = max(max_profit, p)
            difficulty.append(d)
            profit.append(max_profit)
        for w in worker:
            pos = bisect.bisect_right(difficulty, w)
            res += profit[pos - 1] if pos > 0 else 0
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfitAssignment([68, 35, 52, 47, 86],
                                       [67, 17, 1, 81, 3],
                                       [92, 10, 85, 84, 82]))
