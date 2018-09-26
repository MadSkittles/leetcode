class Solution:
    def convertToTitle(self, n):
        n, base, index = n - 1, 26, 1
        while base <= n:
            n -= base
            base *= 26
            index += 1
        res = ''
        for _ in range(index):
            res = chr(65 + n % 26) + res
            n //= 26
        return res
    
    def convertToTitle1(self, n):
        s = ""
        while n:
            s = chr(ord("A") + (n - 1) % 26) + s
            n = (n - 1) // 26
        return s


if __name__ == '__main__':
    solution = Solution()
    print(solution.convertToTitle(1))
    print(solution.convertToTitle(26))
    print(solution.convertToTitle(27))
    print(solution.convertToTitle(28))
    print(solution.convertToTitle(702))
    print(solution.convertToTitle(703))
