from collections import Counter


class Solution:
    def totalFruit(self, tree):
        c, lo, res = Counter(), 0, 0
        for hi in range(len(tree)):
            c[tree[hi]] += 1
            if len(c) > 2:
                res = max(res, hi - lo)
                while len(c) > 2:
                    c[tree[lo]] -= 1
                    if not c[tree[lo]]:
                        c.pop(tree[lo])
                    lo += 1
        res = max(res, hi - lo + 1)
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.totalFruit([1, 2, 1]))
    print(solution.totalFruit([0, 1, 2, 2]))
    print(solution.totalFruit([1, 2, 3, 2, 2]))
    print(solution.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
