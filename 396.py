class Solution:
    def maxRotateFunction(self, A):
        res = float('-inf')
        for i in range(len(A)):
            res = max(res, sum(map(lambda x: x[0] * x[1], zip(A[-i:] + A[:-i], range(len(A))))))
        return res if res != float('-inf') else 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxRotateFunction([-10]))
