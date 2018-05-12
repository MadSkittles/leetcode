class Solution:
    def largestRectangleArea(self, heights: list):
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
    print(solution.largestRectangleArea([2, 1, 5, 6, 2, 3]))
