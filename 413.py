class Solution:
    def numberOfArithmeticSlices(self, A):
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

        return sum(sum(l + 1 - i for i in range(3, l + 1),) for l in lengths)


if __name__ == '__main__':
    solution = Solution()
    print(solution.numberOfArithmeticSlices([]))
