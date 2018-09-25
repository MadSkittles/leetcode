class Solution:
    def shortestPalindrome(self, s):
        A = s + "*" + s[::-1]
        lps = [0]
        for i in range(1, len(A)):
            index = lps[i - 1]
            while index > 0 and A[index] != A[i]:
                index = lps[index - 1]
            lps.append(index + (1 if A[index] == A[i] else 0))
        return s[lps[-1] :][::-1] + s


if __name__ == "__main__":
    solution = Solution()
    print(solution.shortestPalindrome("aacecaaa"))
