class Solution:
    def consecutiveNumbersSum(self, N):
        return sum((i % 2 and not N % i) or (not i % 2 and N % i and not (2 * N) % i) for i in range(1, int((2 * N) ** 0.5) + 1))


if __name__ == '__main__':
    solution = Solution()
    print(solution.consecutiveNumbersSum(4))
    print(solution.consecutiveNumbersSum(5))
    print(solution.consecutiveNumbersSum(9))
    print(solution.consecutiveNumbersSum(15))
