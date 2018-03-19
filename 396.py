# F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1]
# F(k-1) = 0 * Bk-1[0] + 1 * Bk-1[1] + ... + (n-1) * Bk-1[n-1]
#        = 0 * Bk[1] + 1 * Bk[2] + ... + (n-2) * Bk[n-1] + (n-1) * Bk[0]
# F(k) = F(k-1) + sum - nBk[0]
# F(k-1) = F(k) - sum + nBk[0]

class Solution:
    def maxRotateFunction(self, A):
        s = sum(A)
        res = f = sum(i * v for i, v in enumerate(A))
        for i in range(1, len(A)):
            f = f - s + len(A) * A[i - 1]
            res = max(res, f)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxRotateFunction([4, 3, 2, 6]))
