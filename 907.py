class Solution:
    def sumSubarrayMins(self, A):
        n, mod = len(A), 10 ** 9 + 7
        left, right, s1, s2 = [0] * n, [0] * n, [], []
        for i in range(n):
            count = 1
            while s1 and s1[-1][0] > A[i]:
                count += s1.pop()[1]
            left[i] = count
            s1.append([A[i], count])
        for i in range(n)[::-1]:
            count = 1
            while s2 and s2[-1][0] >= A[i]:
                count += s2.pop()[1]
            right[i] = count
            s2.append([A[i], count])
        return sum(a * l * r for a, l, r in zip(A, left, right)) % mod


if __name__ == "__main__":
    solution = Solution()
    print(solution.sumSubarrayMins([3, 1, 2, 4]))

