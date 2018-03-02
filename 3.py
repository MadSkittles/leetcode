# Longest Substring Without Repeating Characters

# Given a string, find the length of the longest substring without repeating characters.

# Examples:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) <= 1:
            return len(s)
        result = -1
        flag = {}
        cur = start = 0
        while cur < len(s):
            if s[cur] not in flag:
                flag[s[cur]] = cur
                cur += 1
            else:
                result = (cur - start) if (cur - start) > result else result
                cur = start = flag[s[cur]] + 1
                flag.clear()
        result = (cur - start) if (cur - start) > result else result
        return result

print(Solution().lengthOfLongestSubstring('pwwkewa'))