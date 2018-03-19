class Solution:
    def reconstructQueue(self, people):
        people.sort(key=lambda x: x[1])
        res = []
        for p in people:
            cnt, i = 0, 0
            while i < len(res):
                if res[i][0] >= p[0]:
                    cnt += 1
                if cnt > p[1]:
                    break
                i += 1
            res.insert(i, p)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
