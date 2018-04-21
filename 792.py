class Solution:
    def numMatchingSubseq(self, S, words):
        self.index_map = {}
        for i, c in enumerate(S):
            self.index_map.setdefault(c, []).append(i)
        return sum(self.isSubsequence(word) for word in words)

    def isSubsequence(self, word):
        import bisect
        index = -1
        for c in word:
            if index > self.index_map.get(c, [float('-inf')])[-1]:
                return False
            index = self.index_map[c][bisect.bisect_left(self.index_map[c], index)] + 1
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.numMatchingSubseq("dsahjpjauf",
                                     ["ahbwzgqnuk"]))
