class Solution:
    def peakIndexInMountainArray(self, A):
        for i, n in enumerate(A):
            if A[i] > A[i + 1]:
                return i


if __name__ == "__main__":
    solution = Solution()
    print(solution.peakIndexInMountainArray([0, 2, 1, 0]))

