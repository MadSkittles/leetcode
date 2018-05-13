class Solution:
    def flipAndInvertImage(self, A):
        return [[1 - n for n in row][::-1] for row in A]


if __name__ == '__main__':
    solution = Solution()
    print(solution.flipAndInvertImage([]))
    print(solution.flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))
