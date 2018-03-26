class Solution:
    def findMaxForm(self, strs, m, n):
        from collections import Counter
        cnts = [Counter(s) for s in strs]
        get, no_get = [(m - cnts[0]['0'], n - cnts[0]['1'], 1)
                       if m > cnts[0]['0'] and n > cnts[0]['1'] else (float('-inf'),) * 3], [
                          (m, n, 0)]
        for s in cnts[1:]:
            res = []
            if get[-1] and get[-1][0] >= s['0'] and get[-1][1] >= s['1']:
                res.append((get[-1][0] - s['0'], get[-1][1] - s['1'], get[-1][2] + 1))
            if no_get[-1][0] >= s['0'] and no_get[-1][1] >= s['1']:
                res.append((no_get[-1][0] - s['0'], no_get[-1][1] - s['1'], no_get[-1][2] + 1))
            no_get.append(max([get[-1], no_get[-1]], key=lambda x: (x[2], x[0], x[1])))
            get.append(max(res, key=lambda x: x[2]) if res else (float('-inf'),) * 3)
        return max(get[-1][2] if get[-1] else float('-inf'), no_get[-1][2])


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMaxForm(
        ["0", "11", "1000", "01", "0", "101", "1", "1", "1", "0", "0", "0", "0", "1", "0", "0110101", "0", "11", "01",
         "00", "01111", "0011", "1", "1000", "0", "11101", "1", "0", "10", "0111"], 9, 80))
