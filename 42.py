class Solution:
    def trap(self, height):
        res, lo = 0, 0
        for hi in range(1, len(height)):
            if height[hi] >= height[lo]:
                x = height[lo]
                while lo < hi:
                    res += x - height[lo]
                    lo += 1
        hi = len(height) - 1
        for lo in range(len(height) - 1)[::-1]:
            if height[lo] > height[hi]:
                x = height[hi]
                while lo < hi:
                    res += x - height[hi]
                    hi -= 1
        return res

if __name__ == '__main__':
    solution=Solution()
    print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
