class Solution:
    def isPalindrome(self, s: str):
        lo, hi = 0, len(s) - 1
        while lo < hi:
            if not s[lo].isalnum():
                lo += 1
            elif not s[hi].isalnum():
                hi -= 1
            elif s[lo].lower() != s[hi].lower():
                return False
            else:
                lo += 1
                hi -= 1
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))
    print(solution.isPalindrome("race a car"))
