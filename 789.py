class Solution:
    def escapeGhosts(self, ghosts, target):
        return abs(target[0]) + abs(target[1]) < min(abs(x - target[0]) + abs(y - target[1]) for x, y in ghosts)


if __name__ == '__main__':
    solution = Solution()
    print(solution.escapeGhosts([[1, 0]], [2, 0]))
