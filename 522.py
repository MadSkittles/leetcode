class Solution:
    def findLUSlength(self, strs: list):
        strs.sort(key=lambda x: len(x))
        self.index_map = []
        for s in strs:
            m = {}
            for index, c in enumerate(s):
                m.setdefault(c, []).append(index)
            self.index_map.append(m)
        res = -1
        for i in range(len(strs)):
            for j in range(len(strs)):
                if i == j:
                    continue
                if len(strs[i]) < len(strs[j]) and self.isSubsequence(strs[i], j):
                    break
                if strs[i] == strs[j]:
                    break
            else:
                res = max(res, len(strs[i]))
        return res

    def isSubsequence(self, s, j):
        import bisect
        m, index = self.index_map[j], -1
        for c in s:
            if index > m.get(c, [float('-inf')])[-1]:
                return False
            index = m[c][bisect.bisect_left(m[c], index)] + 1
        return True
