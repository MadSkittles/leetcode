class Solution:
    def numRabbits(self, answers):
        from collections import Counter
        res, c = 0, Counter(answers)
        for k in c:
            res += (c[k] // (k + 1) + (c[k] % (k + 1) != 0)) * (k + 1)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.numRabbits([1, 1, 2]))
    print(solution.numRabbits([10, 10, 10]))
