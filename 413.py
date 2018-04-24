class Solution:
    def numberOfArithmeticSlices(self, A):
        if len(A) < 3:
            return 0
        lo, hi, diff, res = 0, 1, A[1] - A[0], 0
        for i, v in enumerate(A[2:], 2):
            if v - A[hi] == diff:
                hi += 1
                res += hi - lo - 1
            else:
                lo, hi, diff = hi, i, A[i] - A[i - 1]
        return res

    def numberOfArithmeticSlices1(self, A):
        cnt = 2
        lengths = []
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                cnt += 1
            else:
                if cnt > 2:
                    lengths.append(cnt)
                cnt = 2
        if cnt > 2:
            lengths.append(cnt)

        return sum(sum(l + 1 - i for i in range(3, l + 1), ) for l in lengths)


if __name__ == '__main__':
    solution = Solution()
    print(solution.numberOfArithmeticSlices([1, 2, 3, 4]))
