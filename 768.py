class Solution:
    def maxChunksToSorted(self, arr):
        a = sorted(arr)
        pos = {}
        for i, n in enumerate(a):
            pos.setdefault(n, []).append(i)
        res, right, left, start, end = 0, -1, 2000, 0, 0
        for i, v in enumerate(arr):
            p = pos[v].pop(0)
            right, left = max(right, p), min(left, p)
            if start == left and end == right:
                res += 1
                start = end = i + 1
                right, left = -1, 2000
            else:
                end += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxChunksToSorted([1,0,2,3,4]))
