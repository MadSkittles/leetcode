class Solution:
    def wordBreak(self, s, wordDict):
        dp = [True]
        for i in range(len(s)):
            dp.append(any(dp[j] and s[j:i + 1] in wordDict for j in range(i + 1)))
        if not dp[-1]:
            return []
        dp = [{()}]
        for i in range(len(s)):
            l = set()
            for j in range(i + 1):
                if dp[j] and s[j:i + 1] in wordDict:
                    l.update({v + (s[j:i + 1],) for v in dp[j]})
            dp.append(l)
        return [' '.join(l) for l in dp[-1]]


if __name__ == '__main__':
    solution = Solution()
    print(solution.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
    print(solution.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
    print(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    print(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
