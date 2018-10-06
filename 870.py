from bisect import bisect_right


class Solution:
    def advantageCount(self, A, B):
        res = [None] * len(B)
        A.sort()
        for i, n in enumerate(B):
            p = bisect_right(A, n)
            if p < len(A):
                res[i] = A[p]
                A.pop(p)
        if A:
            for i in range(len(res)):
                if res[i] is None:
                    res[i] = A.pop()
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.advantageCount([2, 7, 11, 15], [1, 10, 4, 11]))
    print(solution.advantageCount([12, 24, 8, 32], [13, 25, 32, 11]))

