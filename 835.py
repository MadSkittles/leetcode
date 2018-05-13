class Solution:
    def largestOverlap(self, A, B):
        from collections import Counter
        N = len(A)
        cord_A, cord_B = [(i, j) for i in range(N) for j in range(N) if A[i][j]], [(i, j) for i in range(N) for j in range(N) if B[i][j]]
        cnt = Counter((iA - iB, jA - jB) for iA, jA in cord_A for iB, jB in cord_B)
        return max(cnt.values(), default=0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestOverlap([[0, 1], [1, 1]],
                                  [[1, 1], [1, 0]]))
