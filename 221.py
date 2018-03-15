# DP DP数组中的DP[i][j]代表了以（i，j）为右下角的square的边长。所以当matrix[i][j]==1时，DP[i][j]=min(DP[i-1][j],DP[i][j-1],DP[i-1][j-1]),
# 因为这三者中有一个为0时，matrix[i][j]并不能使某个square扩大。而这三者大于0，只能是其中最小值所在的square扩大。

class Solution:
    def maximalSquare(self, matrix):
        res = 0
        for i, row in enumerate(matrix):
            for j, v in enumerate(row):
                if v == '1':
                    matrix[i][j] = min(matrix[i - 1][j] if i > 0 else 0, matrix[i][j - 1] if j > 0 else 0,
                                       matrix[i - 1][j - 1] if i > 0 and j > 0 else 0) + 1
                    res = max(res, matrix[i][j])
                else:
                    matrix[i][j] = int(v)
        return res ** 2


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximalSquare([['0']]))
