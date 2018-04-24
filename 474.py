class Solution:
    def findMaxForm(self, strs, m, n):
        from collections import Counter
        str_cnts = [Counter(s) for s in strs]
        select = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(len(strs)):
            cnt_0, cnt_1 = str_cnts[i]['0'], str_cnts[i]['1']
            for j in range(m, -1, -1):
                for k in range(n, -1, -1):
                    if j >= cnt_0 and k >= cnt_1 and select[j][k] < select[j - cnt_0][k - cnt_1] + 1:
                        select[j][k] = select[j - cnt_0][k - cnt_1] + 1
        return select[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))
    print(solution.findMaxForm(["10", "0", "1"], 1, 1))
