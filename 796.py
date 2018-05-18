class Solution:
    def rotateString(self, A, B):
        if len(A) != len(B):
            return False
        return A in (B * 2)


if __name__ == '__main__':
    solution = Solution()
    print(solution.rotateString(A='abcde', B='cdeab'))
    print(solution.rotateString(A='abcde', B='abced'))
