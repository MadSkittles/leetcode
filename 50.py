class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n % 2:
                pow *= x
            x *= x
            n //= 2
        return pow


if __name__ == '__main__':
    solution = Solution()
    print(solution.myPow(22.14659, -2))
    print(solution.myPow(2.1, 3))
    print(solution.myPow(34.00515, -3))
    print(solution.myPow(62.23270, -1))
