class Solution:
    def kthSmallestPrimeFraction(self, A, K):
        import bisect
        l, r = 0, 1
        while l < r:
            m = (l + r) / 2
            cnt = [bisect.bisect_right(A, A[i] * m, 0, i) for i in range(1, len(A))]
            c = sum(cnt)
            if c < K:
                l = m
            elif c > K:
                r = m
            else:
                return max([[A[j - 1], A[i]] for i, j in enumerate(cnt, 1) if j], key=lambda x: x[0] / x[1])


if __name__ == '__main__':
    solution = Solution()
    print(solution.kthSmallestPrimeFraction([1, 7], 1))
