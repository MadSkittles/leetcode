class Solution:
    def isUgly(self, num):
        for n in [2, 3, 5]:
            while num > 1 and num % n == 0:
                num //= n
        return num == 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.isUgly(1))
    print(solution.isUgly(2))
    print(solution.isUgly(3))
    print(solution.isUgly(5))
    print(solution.isUgly(6))
    print(solution.isUgly(8))
    print(solution.isUgly(14))
