class Solution:
    def medianSlidingWindow(self, nums, k):
        import bisect
        if not nums or k == 1:
            return [n / 1. for n in nums]
        is_odd = bool(k & 1)
        window = sorted(nums[:k])
        res = [window[len(window) // 2] / 1. if is_odd else (window[len(window) // 2] + window[len(window) // 2 - 1]) / 2.]
        for i in range(k, len(nums)):
            window.pop(bisect.bisect_left(window, nums[i - k]))
            bisect.insort(window, nums[i])
            res.append(window[k // 2] / 1. if is_odd else (window[k // 2] + window[k // 2 - 1]) / 2.)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7],
                                       3))
