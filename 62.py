class Solution_Not_Satisfied:
    def uniquePaths(self, m, n):
        self.cache = {}
        return self.f(m - 1, n - 1)

    def f(self, down_left, right_left):
        cache = self.cache.get((down_left, right_left)) or self.cache.get((right_left, down_left))
        if cache:
            return cache

        if down_left == 0 or right_left == 0:
            res = 1
        else:
            res = self.f(down_left - 1, right_left) + self.f(down_left, right_left - 1)

        if (down_left, right_left) not in self.cache:
            self.cache[(down_left, right_left)] = res
        return res


class Solution:
    def uniquePaths(self, m, n):
        m -= 1
        n -= 1
        max_num = max(m, n)
        min_num = m + n - max_num
        sum = 1
        index = 1
        for i in range(max_num + 1, m + n + 1):
            sum *= i
            while index <= min_num:
                if sum % index == 0:
                    sum //= index
                    index += 1
                else:
                    break
        return sum


if __name__ == '__main__':
    solution = Solution()
    solution1 = Solution_Not_Satisfied()
    print(solution.uniquePaths(100, 100))
    print(solution1.uniquePaths(100, 100))
