<<<<<<< HEAD
class Solution:
    def integerBreak(self, n):
        res = [0, 1, 1]
        for i in range(3, n + 1):
            half = i // 2
            res.append(max(max(j, res[j]) * max(i - j, res[i - j]) for j in range(1, half + 1)))
        return res[-1]
=======
class Solution:
    def integerBreak(self, n):
        res = [0, 1, 1]
        for i in range(3, n + 1):
            res.append(max(max(j, res[j]) * max(i - j, res[i - j]) for j in range(1, i // 2 + 1)))
        return res[-1]


if __name__ == '__main__':
    solution = Solution()
    for i in range(2, 20):
        print(i, solution.integerBreak(i))
    print(58, solution.integerBreak(58))
>>>>>>> e97303ba85e315aed3ace5a2999b55ac9be2b357
