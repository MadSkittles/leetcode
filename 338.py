class Solution:
    def countBits(self, num):
        res = [0]
        n = 0
        for i in range(1, num + 1):
            if i == 2 ** n:
                res.append(1)
                n += 1
            else:
                res.append(1 + res[i - 2 ** (n - 1)])
        return res


if __name__ == '__main__':
    solution = Solution()
    res = solution.countBits(100)
    for i in range(101):
        print(i, sum(map(int, bin(i)[2:])), res[i])
