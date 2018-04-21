class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        max_ = float('-inf')
        res = p = lo = hi = 0
        for i, v in enumerate(A):
            max_ = max(max_, v)
            if L <= max_ <= R:
                hi += 1
                if v >= L:
                    res += hi - lo
                    p = i
                else:
                    res += p - lo + 1
            elif max_ > R:
                p = lo = hi = i + 1
                max_ = float('-inf')
            else:
                hi += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.numSubarrayBoundedMax(
        [876, 880, 482, 260, 132, 421, 732, 703, 795, 420, 871, 445, 400, 291, 358, 589, 617, 202, 755, 810, 227, 813, 549, 791, 418, 528, 835, 401, 526, 584, 873, 662, 13, 314, 988, 101, 299, 816, 833, 224, 160, 852, 179, 769, 646, 558, 661, 808, 651, 982, 878, 918, 406, 551, 467, 87, 139, 387, 16,
         531, 307, 389, 939, 551, 613, 36, 528, 460, 404, 314, 66, 111, 458, 531, 944, 461, 951, 419, 82, 896, 467, 353, 704, 905, 705, 760, 61, 422, 395, 298, 127, 516, 153, 299, 801, 341, 668, 598, 98, 241],
        658,
        719))
