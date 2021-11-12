from typing import List
from bisect import bisect


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        for i in range(1, len(nums))[::-1]:
            if nums[i] > nums[i - 1]:
                nums[i:] = nums[i:][::-1]
                pos = bisect(nums, nums[i - 1], i)
                nums[i - 1], nums[pos] = nums[pos], nums[i - 1]
                return
        else:
            nums[:] = nums[::-1]


if __name__ == '__main__':
    from itertools import permutations

    solution = Solution()
    p = list(permutations([1, 2, 3, 4, 5]))
    for i in range(len(p)):
        d = list(p[i]).copy()
        solution.nextPermutation(d)
        print(p[(i + 1) % len(p)], d)
