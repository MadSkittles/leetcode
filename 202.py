class Solution:
    def isHappy(self, n):
        shown = set()
        while n != 1 and n not in shown:
            shown.add(n)
            s, m = 0, n
            while m:
                s += (m % 10) ** 2
                m //= 10
            n = s
        return n == 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.isHappy(19))
