class Solution:
    def monotoneIncreasingDigits(self, N):
        from itertools import accumulate
        self.N = []
        while N:
            self.N.append(N % 10)
            N //= 10
        self.N = self.N[::-1]
        self.s = [*accumulate(self.N, lambda x, y: x * 10 + y)]
        return self.f(0, 0, False)

    def f(self, index, sum, to9):
        if index >= len(self.N):
            return sum
        pre_digit = sum % 10
        for i in range(9 if to9 else self.N[index], pre_digit - 1, -1):
            if sum * 10 + i <= self.s[index]:
                res = self.f(index + 1, sum * 10 + i, to9 or i < self.s[index])
                if res:
                    return res
        return None


if __name__ == '__main__':
    solution = Solution()
    print(solution.monotoneIncreasingDigits(1000000000))
