class Solution:
    def combinationSum(self, candidates, target):
        result = set()
        self.f(result, target, 0, candidates, 0, tuple())
        return [list(s) for s in result]

    def f(self, result, target, index, candidates, sum, cur_list):
        if sum == target:
            result.add(cur_list)
            return
        if index >= len(candidates) or sum > target:
            return

        if sum + candidates[index] <= target:
            self.f(result, target, index, candidates, sum + candidates[index], (*cur_list, candidates[index]))
            self.f(result, target, index + 1, candidates, sum + candidates[index], (*cur_list, candidates[index]))
        self.f(result, target, index + 1, candidates, sum, cur_list)


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum([2, 3, 6, 7], 7))
