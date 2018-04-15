class Solution:
    def partitionLabels(self, S):
        pos = {}
        for i, c in enumerate(S):
            if c in pos:
                pos[c][1] = i
            else:
                pos[c] = [i, i]
        p = sorted(pos.values())
        res, l, cur_end = [], 0, 0
        for start, end in p:
            if start > cur_end:
                res.append(cur_end)
            cur_end = max(end, cur_end)
        res = [-1] + res + [len(S) - 1]
        return [res[i] - res[i - 1] for i in range(1, len(res))]