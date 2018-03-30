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
        m = self.index_map[j]
        cur = -1
        for c in s:
            if c not in m:
                return False
            else:
                index = m[c]
                for i in index:
                    if i > cur:
                        cur = i
                        break
                else:
                    return False
        return True