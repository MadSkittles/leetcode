class Solution:
    def splitArraySameAverage(self, A):
        s = sum(A)
        dp = [set() for _ in range(len(A) // 2 + 1)]
        dp[0].add(0)
        for n in A:
            for i in range(1, len(dp))[::-1]:
                if dp[i - 1]:
                    dp[i].update({v + n for v in dp[i - 1]})
                if any(v * len(A) == s * i for v in dp[i]):
                    return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.splitArraySameAverage([1, 2, 3, 4, 5, 6, 7, 8]))
