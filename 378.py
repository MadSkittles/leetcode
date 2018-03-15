class Solution:
    def kthSmallest(self, matrix, k):
        import bisect
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = (lo + hi) // 2
            if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def kthSmallest1(self, matrix, k):
        import heapq
        from itertools import chain
        return heapq.nsmallest(k, chain(*matrix))[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.kthSmallest([
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ], 8))
