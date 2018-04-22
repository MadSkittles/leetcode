class Solution:
    def minSwap(self, A, B):
        dp = [(0, 1)]
        for i in range(1, len(A)):
            if min(A[i], B[i]) > max(A[i - 1], B[i - 1]):
                c = (min(dp[i - 1]), min(dp[i - 1]) + 1)
            elif A[i] > A[i - 1] and B[i] > B[i - 1]:
                c = (dp[i - 1][0], dp[i - 1][1] + 1)
            else:
                c = (dp[i - 1][1], dp[i - 1][0] + 1)
            dp.append(c)
        return min(dp[-1])


if __name__ == '__main__':
    solution = Solution()
    print(solution.minSwap([0, 3, 5, 8, 9],
                           [2, 1, 4, 6, 9]))
