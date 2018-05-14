class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words or not words[0]:
            return []
        from collections import Counter
        n = len(s)
        k = len(words[0])
        t = len(words) * k
        req = Counter(words)
        ans = []
        for i in range(min(k, n - t + 1)):
            self._findSubstring(i, i, n, k, t, s, req, ans)
        return ans

    def _findSubstring(self, l, r, n, k, t, s, req, ans):
        curr = {}
        while r + k <= n:
            w = s[r:r + k]
            r += k
            if w not in req:
                l = r
                curr.clear()
            else:
                curr[w] = curr[w] + 1 if w in curr else 1
                while curr[w] > req[w]:
                    curr[s[l:l + k]] -= 1
                    l += k
                if r - l == t:
                    ans.append(l)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findSubstring("abcdefghij",
                                 ["gh", "ij"]))
