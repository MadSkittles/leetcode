class Solution:
    def matrixScore(self, A):
        N, M = len(A), len(A[0])
        for i in range(N):
            if A[i][0] == 0:
                A[i] = [1 - n for n in A[i]]
        res = 0
        for i in range(M):
            one_num = sum(A[j][i] for j in range(N))
            res += (2 ** (M - 1 - i)) * max(one_num, N - one_num)
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]))

