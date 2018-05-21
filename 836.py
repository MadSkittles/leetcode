class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        return not (rec2[1] >= rec1[3] or rec2[0] >= rec1[2] or rec2[3] <= rec1[1] or rec2[2] <= rec1[0])


if __name__ == '__main__':
    solution = Solution()
    print(solution.isRectangleOverlap(rec1=[0, 0, 1, 1], rec2=[1, 0, 2, 1]))
