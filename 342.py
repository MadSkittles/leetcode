class Solution:
    def isPowerOfFour(self, num):
        return num > 0 and num & 0x55555555 == num & -num == num


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPowerOfFour(8388608))
