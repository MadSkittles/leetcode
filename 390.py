class Solution:
    def lastRemaining(self, n):
        head, step, remaining, left = 1, 1, n, True
        while remaining > 1:
            if left or remaining & 1:
                head += step
            remaining //= 2
            step *= 2
            left = not left
        return head


if __name__ == '__main__':
    solution = Solution()
    print(solution.lastRemaining(9))
