class Solution:
    def integerBreak(self, n):
        res = [0, 1, 1]
        for i in range(3, n + 1):
            half = i // 2
            res.append(max(max(j, res[j]) * max(i - j, res[i - j]) for j in range(1, half + 1)))
        return res[-1]