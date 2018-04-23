class Solution:
    def flipgame(self, fronts, backs):
        s = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                s.add(fronts[i])
        res = float('inf')
        for v in fronts + backs:
            if v < res and v not in s:
                res = v
        return res if res < float('inf') else 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.flipgame([1, 2, 4, 4, 7], [1, 3, 4, 1, 3]))
