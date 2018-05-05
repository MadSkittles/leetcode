class Solution(object):
    def countPrimes(self, n):
        flag = [False, False] + [True] * (n - 2)
        for i in range(2, n // 2 + 1):
            if flag[i]:
                j = i * 2
                while j < n:
                    flag[j] = False
                    j += i
        return sum(flag)


if __name__ == '__main__':
    solution = Solution()
    print(solution.countPrimes(7))
