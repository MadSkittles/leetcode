class Solution:
    def longestCommonPrefix(self, strs):
        trie = {}
        for s in strs:
            parent = trie
            for c in s:
                parent = parent.setdefault(c, {})
            parent['#'] = None
        res, parent = '', trie
        while len(parent) == 1 and '#' not in parent:
            key, parent = parent.popitem()
            res += key
        return res

    def longestCommonPrefix1(self, strs):
        if not strs:
            return ''
        s1, s2 = min(strs), max(strs)
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(["dog", "racecar", "car"]))
