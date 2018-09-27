class Solution:
    def rangeBitwiseAnd(self, m, n):
        c = min(i for i in range(33) if m >> i == n >> i)
        return m >> c << c


if __name__ == "__main__":
    solution = Solution()
    print(solution.rangeBitwiseAnd(5, 7))
