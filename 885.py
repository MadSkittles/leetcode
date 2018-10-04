class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        n, res = 1, [[r0, c0]]
        while True:
            start_x, start_y, length = r0 - n + 1, c0 + n, 2 * n + 1
            l = []
            for i in range(0, length - 1):
                l.append([start_x + i, start_y])
            for i in range(0, length - 1):
                l.append([start_x + length - 2, start_y - 1 - i])
            for i in range(0, length - 1):
                l.append([start_x + length - 3 - i, start_y - length + 1])
            for i in range(0, length - 1):
                l.append([start_x - 1, start_y - length + 2 + i])
            l = [*filter(lambda p: 0 <= p[0] < R and 0 <= p[1] < C, l)]
            if not l:
                break
            else:
                res.extend(l)
                n += 1
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.spiralMatrixIII(R=5, C=6, r0=1, c0=4))

