class Solution:
    def longestSubstring(self, s, k):
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)

    # def longestSubstring1(self, s, k):
    #     from collections import Counter,deque
    #     cnt = Counter(s)
    #     start, end = 0, len(s) - 1
    #     while start <= end:


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestSubstring('ababbc', 2))
