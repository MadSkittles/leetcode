class Solution:
    def sortArrayByParity(self, A):
        lo, hi = 0, len(A) - 1
        while lo < hi:
            while lo < hi and not A[lo] & 1:
                lo += 1
            while lo < hi and A[hi] & 1:
                hi -= 1
            A[lo], A[hi] = A[hi], A[lo]
        return A


if __name__ == "__main__":
    solution = Solution()
    print(solution.sortArrayByParity([3, 1, 2, 4]))
