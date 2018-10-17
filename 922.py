class Solution:
    def sortArrayByParityII(self, A):
        even_p, odd_p = 0, 1
        for i in range(len(A)):
            even_p, odd_p = max(i + 2 - (i & 1), even_p), max(i + 1 + (i & 1), odd_p)
            while i & 1 and not A[i] & 1:
                A[i], A[even_p] = A[even_p], A[i]
                even_p += 2
            while not i & 1 and A[i] & 1:
                A[i], A[odd_p] = A[odd_p], A[i]
                odd_p += 2
        return A


if __name__ == '__main__':
    solution = Solution()
    print(solution.sortArrayByParityII([4, 2, 5, 7]))
