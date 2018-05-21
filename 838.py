class Solution:
    def pushDominoes(self, dominoes):
        actions = [*filter(lambda x: x[1] != '.', enumerate(dominoes))]
        if not actions:
            return dominoes
        res = ''
        if actions[0][1] == 'L':
            res += 'L' * actions[0][0]
        else:
            res += '.' * actions[0][0]
        for i in range(1, len(actions)):
            if actions[i][1] == 'L':
                if actions[i - 1][1] == 'R':
                    l = (actions[i][0] - actions[i - 1][0]) // 2
                    if (actions[i][0] - actions[i - 1][0]) % 2 == 0:
                        res += 'R' * l + '.' + 'L' * (l - 1)
                    else:
                        res += 'R' * (l + 1) + 'L' * l
                if actions[i - 1][1] == 'L':
                    res += 'L' * (actions[i][0] - actions[i - 1][0])
            if actions[i][1] == 'R':
                if actions[i - 1][1] == 'R':
                    res += 'R' * (actions[i][0] - actions[i - 1][0])
                else:
                    res += 'L' + '.' * (actions[i][0] - actions[i - 1][0] - 1)
        if actions[-1][1] == 'R':
            res += 'R' * (len(dominoes) - actions[-1][0])
        else:
            res += 'L' + '.' * (len(dominoes) - actions[-1][0] - 1)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.pushDominoes('.L.R...LR..L..'))
    print(solution.pushDominoes('.'))
