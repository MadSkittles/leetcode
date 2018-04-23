class Solution:
    def canTransform(self, start, end):
        s, e = [(v, i) for i, v in enumerate(start) if v != 'X'], [(v, i) for i, v in enumerate(end) if v != 'X']
        return len(s) == len(e) and all(c1 == c2 and ((c1 == 'L' and i >= j) or (c1 == 'R' and i <= j)) for (c1, i), (c2, j) in zip(s, e))


if __name__ == '__main__':
    solution = Solution()
    print(solution.canTransform('RXXLRXRXL', 'XRLXXRRLX'))
