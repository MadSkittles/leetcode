# Longest Palindromic Substring

# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Input: "cbbd"
# Output: "bb"

# Manacher's Algorithm !!!!

class Solution:
    def longestPalindrome(self, s):
        s = '#' + '#'.join(s) + '#'
        RL = [0] * len(s)
        max_right = 0
        pos = 0
        max_substring = None
        max_length = -1

        for i in range(len(s)):
            if i < max_right and max_right - i > RL[2 * pos - i]:
                RL[i] = RL[2 * pos - i]
            else:
                p = i + 1
                while (2 * i - p) >= 0 and p < len(s) and s[p] == s[2 * i - p]:
                    p += 1
                RL[i] = p - i
                max_right = p - 1
                pos = i

            if RL[i] > max_length:
                max_substring = s[i - RL[i] + 1:i] + s[i:i + RL[i]]
                max_length = RL[i]

        return max_substring[1::2]


if __name__ == '__main__':
    print(Solution().longestPalindrome('cbbd'))
    print(Solution().longestPalindrome('abba'))
