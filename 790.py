class Solution:
    def numTilings(self, N):
        m = [1, 1, 2]
        if N < 3:
            return m[N]
        s = sum(m[:2])
        for i in range(3, N + 1):
            s += m[i - 3] + m[i - 1]
            m.append(s % (10 ** 9 + 7))
        return m[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.numTilings(1000))
