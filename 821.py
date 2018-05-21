class Solution:
    def shortestToChar(self, S, C):
        index = [i for i, c in enumerate(S) if c == C]
        res, i = [], 0
        for j, c in enumerate(S):
            if i < len(index) and j == index[i]:
                res.append(0)
                i += 1
                continue
            if i == 0:
                res.append(index[i] - j)
            elif 0 < i < len(index):
                res.append(min(j - index[i - 1], index[i] - j))
            else:
                res.append(j - index[i - 1])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.shortestToChar("aaba", "b"))
