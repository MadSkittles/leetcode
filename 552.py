class Solution:
    def findKthNumber(self, m, n, k):
        m, n = min(m, n), max(m, n)
        l, r = 1, m * n
        while l < r:
            mid = (l + r) // 2
            cnt = sum(min(n, mid // i) for i in range(1, m + 1))
            if cnt >= k:
                r = mid
            else:
                l = mid + 1
        return l


if __name__ == '__main__':
    solution = Solution()
    print(solution.findKthNumber(m=3, n=3, k=5))
