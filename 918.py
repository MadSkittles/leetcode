class Solution:
    def maxSubarraySumCircular(self, A):
        total, max_sum, cur_max, min_sum, cur_min = 0, -float("inf"), 0, float("inf"), 0
        for a in A:
            cur_max, cur_min = max(cur_max + a, a), min(cur_min + a, a)
            max_sum, min_sum = max(max_sum, cur_max), min(min_sum, cur_min)
            total += a
        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubarraySumCircular([1, -2, 3, -2]))
    print(solution.maxSubarraySumCircular([5, -3, 5]))
    print(solution.maxSubarraySumCircular([3, -1, 2, -1]))
    print(solution.maxSubarraySumCircular([3, -2, 2, -3]))
    print(solution.maxSubarraySumCircular([-2, -3, -1]))

