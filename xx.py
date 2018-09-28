class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack, res = [], [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                j, tt = stack.pop()
                res[j] = i - j
            stack.append((i, t))
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
