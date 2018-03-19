class Solution:
    def integerReplacement(self, n):
        step = [0] * (n + 2)
        step[2] = 1
        for i in range(2, n + 1):
            if step[n] != 0:
                break
            if i & 1:
                step[i] = min(step[i - 1], step[i + 1]) + 1
            if 2 * i < len(step):
                step[2 * i] = step[i] + 1
        return step[n]


if __name__ == '__main__':
    solution = Solution()
    for i in range(1, 129):
        print(i, solution.integerReplacement(i))
