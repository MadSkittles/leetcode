class Solution:
    def maxChunksToSorted(self, arr):
        cnt, res, max_num, min_num, start, end = 0, 0, -1, 10, 0, 0
        for i, v in enumerate(arr):
            max_num, min_num = max(max_num, v), min(min_num, v)
            if start == min_num and end == max_num:
                res += 1
                start = end = i + 1
                max_num, min_num = -1, 10
            else:
                end += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxChunksToSorted([0, 2, 1, 4, 3]))
    print(solution.maxChunksToSorted([4, 3, 2, 1, 0]))
    print(solution.maxChunksToSorted([1, 0, 2, 3, 4]))
