class Solution:
    def findClosestElements(self, arr, k, x):
        from bisect import bisect_left
        pos = bisect_left(arr, x)
        hi, lo, res_low, res_high = pos, pos - 1, [], []
        while (lo >= 0 or hi < len(arr)) and len(res_low) + len(res_high) < k:
            if (lo >= 0 and hi < len(arr) and abs(arr[lo] - x) <= abs(arr[hi] - x)) or hi >= len(arr):
                res_low.append(arr[lo])
                lo -= 1
            else:
                res_high.append(arr[hi])
                hi += 1
        return res_low[::-1] + res_high


if __name__ == '__main__':
    solution = Solution()
    print(solution.findClosestElements([1, 2, 3, 4, 5], 4, 3))
    print(solution.findClosestElements([1, 2, 3, 4], 4, -1))
