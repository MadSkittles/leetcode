class Solution:
    def longestMountain(self, A):
        left, right = [], []
        for i, n in enumerate(A):
            if i == 0 or n <= A[i - 1]:
                left.append(0)
            else:
                left.append(left[-1] + 1)
        A = A[::-1]
        for i, n in enumerate(A):
            if i == 0 or n <= A[i - 1]:
                right.append(0)
            else:
                right.append(right[-1] + 1)
        right.reverse()
        return max([left[i] + right[i] + 1 for i in range(len(A)) if left[i] > 0 and right[i] > 0], default=0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestMountain([2, 3]))
