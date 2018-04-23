class Solution:
    def numFactoredBinaryTrees(self, A):
        res, A, cnt = 0, sorted(A), [1] * len(A)
        d = {v: i for i, v in enumerate(A)}
        for i in range(len(A)):
            for j in range(i):
                if A[i] % A[j] == 0 and (A[i] // A[j]) in d:
                    cnt[i] = (cnt[i] + cnt[j] * cnt[d[A[i] // A[j]]]) % (10 ** 9 + 7)
            res = (res + cnt[i]) % (10 ** 9 + 7)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.numFactoredBinaryTrees([2, 4]))
    print(solution.numFactoredBinaryTrees([2, 4, 5, 10]))
