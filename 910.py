class Solution:
    def smallestRangeII(self, A, K):
        A.sort()
        res = min([max(A[-1], A[i] + 2 * K) - min(A[i + 1], A[0] + 2 * K) for i in range(len(A) - 1)] + [A[-1] - A[0]])
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestRangeII([7, 8, 8], 5))

