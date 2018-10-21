from functools import reduce


class Solution:
    def minFlipsMonoIncr(self, S):
        return min(reduce(lambda x, y: (x[0], min(x[0] + 1, x[1] + 1)) if y == "0" else (x[0] + 1, min(x[0], x[1])), S, (0, 0)))


if __name__ == "__main__":
    solution = Solution()
    print(solution.minFlipsMonoIncr("00110"))
    print(solution.minFlipsMonoIncr("010110"))
    print(solution.minFlipsMonoIncr("00011000"))
