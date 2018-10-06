class Solution:
    def partitionDisjoint(self, A):
        max_val, max_l, min_val, min_l = float("-inf"), [None] * len(A), float("inf"), [None] * len(A)
        for i in range(len(A)):
            max_l[i] = max_val = max(max_val, A[i])
            min_l[-1 - i] = min_val = min(min_val, A[-1 - i])
        for i in range(len(A) - 1):
            if max_l[i] <= min_l[i + 1]:
                return i + 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.partitionDisjoint([5, 0, 3, 8, 6]))
    print(solution.partitionDisjoint([1, 1, 1, 0, 6, 12]))

