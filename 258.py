class Solution:
    def addDigits(self, num):
        return [9, 1, 2, 3, 4, 5, 6, 7, 8][num % 9] if num > 0 else 0


if __name__ == '__main__':
    solution = Solution()
    for i in range(100):
        print(i, solution.addDigits(i))
