class Solution:
    def reverseOnlyLetters(self, S):
        S = list(S)
        lo, hi = 0, len(S) - 1
        while lo < hi:
            while not S[lo].isalpha() and lo < hi:
                lo += 1
            while not S[hi].isalpha() and lo < hi:
                hi -= 1
            S[lo], S[hi] = S[hi], S[lo]
            lo += 1
            hi -= 1
        return ''.join(S)


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseOnlyLetters('ab-cd'))
    print(solution.reverseOnlyLetters('a-bC-dEf-ghIj'))
    print(solution.reverseOnlyLetters('Test1ng-Leet=code-Q!'))
