class Solution:
    def customSortString(self, S, T):
        d = {c: i for i, c in enumerate(S)}
        return ''.join(sorted(T, key=lambda x: d.get(x, 27)))


if __name__ == '__main__':
    solution = Solution()
    print(solution.customSortString('cba', 'abcd'))
