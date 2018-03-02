class Solution:
    def permute(self, nums):
        self.result = set()
        self.f(tuple(), nums)
        return self.result

    def f(self, cur_res, candidates):
        if len(cur_res) >= len(candidates):
            self.result.add(cur_res)
            return
        for i in range(len(candidates)):
            n = candidates[i]
            if n is None:
                continue
            candidates[i] = None
            self.f((*cur_res, n), candidates)
            candidates[i] = n


if __name__ == '__main__':
    solution = Solution()
    print(solution.permute([1, 3, 2]))
