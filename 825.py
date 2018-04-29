class Solution:
    def numFriendRequests(self, ages: list):
        from collections import Counter
        ages.sort(reverse=True)
        res, end, c = 0, -1, Counter(ages)
        for i in range(len(ages) - 1):
            end = max(end, i + 1)
            while end < len(ages) and ages[end] > 0.5 * ages[i] + 7:
                end += 1
            res += end - i - 1
        return res + sum((c[k] * (c[k] - 1)) // 2 for k in c if c[k] > 1 and k > 14)


if __name__ == '__main__':
    solution = Solution()
    print(solution.numFriendRequests([73, 106, 39, 6, 26, 15, 30, 100, 71, 35, 46, 112, 6, 60, 110]))
    # print(solution.numFriendRequests([16, 17, 18]))
    # print(solution.numFriendRequests([20, 30, 100, 110, 120]))
