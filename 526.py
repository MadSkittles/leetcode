class Solution:
    def countArrangement(self, N):
        self.N, self.candidates, self.flag = N, {}, {i: False for i in range(1, N + 1)}
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if i % j == 0 or j % i == 0:
                    self.candidates.setdefault(i, []).append(j)
        print(self.candidates)
        return self.f(1)

    def f(self, index):
        if index > self.N:
            return 1
        res = 0
        for i in self.candidates[index]:
            if not self.flag[i]:
                self.flag[i] = True
                res += self.f(index + 1)
                self.flag[i] = False
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.countArrangement(15))
