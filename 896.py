from operator import le, ge, eq


class Solution:
    def isMonotonic(self, A):
        if A[0] == A[-1]:
            func = eq
        elif A[0] < A[-1]:
            func = le
        else:
            func = ge
        return all(func(x, y) for x, y in zip(A, A[1:]))


if __name__ == "__main__":
    solution = Solution()
    print(solution.isMonotonic([1, 2, 2, 3]))
    print(solution.isMonotonic([6, 5, 4, 4]))
    print(solution.isMonotonic([1, 3, 2]))
    print(solution.isMonotonic([1, 2, 4, 5]))
    print(solution.isMonotonic([1, 1, 1]))
    print(solution.isMonotonic([1]))
