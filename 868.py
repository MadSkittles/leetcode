class Solution:
    def binaryGap(self, N):
        res, p = 0, None
        for i in range(32):
            if N & 1:
                if p is not None:
                    res = max(res, i - p)
                p = i
            N >>= 1
        return res if p is not None else 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.binaryGap(5))
