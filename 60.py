class Solution:
    def getPermutation(self, n, k):
        candidates = list(range(1, n + 1))
        factorial = [362880, 40320, 5040, 720, 120, 24, 6, 2, 1][-n:]
        k -= 1
        result = ''
        for i in range(1, len(factorial)):
            n = factorial[i]
            x = candidates[k // n]
            result += str(x)
            candidates.remove(x)
            k = k % n
        result += str(candidates[-1])
        return result


if __name__ == '__main__':
    solution = Solution()
    for i in range(1, 7):
        print(solution.getPermutation(9, i))
