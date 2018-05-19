class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        res, heights = 0, [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            res = max(res, self.largestRectangleArea(heights))
        return res

    def largestRectangleArea(self, heights):
        res, stack, index = 0, [], 0
        heights.append(0)
        while index < len(heights):
            if not stack or heights[index] > stack[-1][1]:
                stack.append((index, heights[index]))
            else:
                x = stack.pop()[1]
                dist = index - stack[-1][0] - 1 if stack else index
                res = max(res, dist * x)
                index -= 1
            index += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximalRectangle([
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]))
