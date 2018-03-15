class Solution:
    def countNumbersWithUniqueDigits(self, n):
        c = [1, 9, 81, 648, 4536, 27216, 136080, 544320, 1632960, 3265920, 3265920]
        return sum(c[:min(n + 1, 11)])


if __name__ == '__main__':
    solution = Solution()
    for i in range(20):
        print(i, solution.countNumbersWithUniqueDigits(i))
