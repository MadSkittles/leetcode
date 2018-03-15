class Solution:
    def lastRemaining(self, n):
        index, n = 1, list(range(1, n + 1))
        while len(n) > 1:
            if index & 1:
                n = n[1::2]
            else:
                n = n[len(n)-2::-2][::-1]
            index += 1
        return n[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.lastRemaining(9))
