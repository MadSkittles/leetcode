class Solution:
    def matrixReshape(self, nums, r, c):
        if not nums:
            return nums
        R, C = len(nums), len(nums[0])
        if not r * c == R * C:
            return nums
        index, res = 0, []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(nums[index // C][index % C])
                index += 1
            res.append(row)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.matrixReshape([[1, 2, 3, 4]],
                                 2,
                                 2))
